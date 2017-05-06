if input == "":

    import collections
    import math
    import random

    gamma = random.gammavariate
    sqrt = math.sqrt
    log = math.log
    R, P, S = 0, 1, 2
    index = {"R": R, "P": P, "S": S}
    beat = (P, S, R)
    name = ("R", "P", "S")

    def ucb(s, n, t):
        return (s / n) + sqrt(2 * log(t) / n)

    class MarkovTree:
        def __init__(self, counts = None):
            self.counts = [0.0 for _ in xrange(3)]
            self.visits = [0.0 for _ in xrange(3)]
            self.children = None

        def score(self, t):
            return ucb(self.pos_total, self.neg_total, self.total_visits, t)

        def select_move(self, t):
            r = gamma(self.counts[0] + 1, 1)
            p = gamma(self.counts[1] + 1, 1)
            s = gamma(self.counts[2] + 1, 1)
            scores = [s - p, r - s, p - r]
            scores = [ucb(s, n + 1, t) for s, n in zip(scores, self.visits)]
            best = max(scores)
            return (best, scores.index(best))

        def update(self, h, i):
            for n in h:
                self.counts[i] += 1
                if self.children is None:
                    break
                self = self.children[n]
                if self is None:
                    break

        def predict(self, h):
            path = []
            stop = False
            path.append(self)
            for d, n in enumerate(h):
                if stop or d >= 16:
                    break
                if self.children is None:
                    self.children = [None for _ in xrange(3)]
                if self.children[n] is None:
                    self.children[n] = MarkovTree()
                    stop = True
                child = self.children[n]
                self = child
                path.append(self)
            t = sum(3 + sum(node.visits) for node in path)
            best_score = float("-inf")
            for i, n in enumerate(path):
                score, move = n.select_move(t)
                if score >= best_score:
                    j = i
                    best_score = score
                    best_node = n
                    best_move = move
            return (best_node, best_move)

    tree = MarkovTree()
    history = collections.deque([])

    node = tree

else:

    i = index[input]
    j = index[output]

    node.visits[j] += 1
    tree.update(history, i)

    history.appendleft(i)
    history.appendleft(j)

node, k = tree.predict(history)
output = name[k]