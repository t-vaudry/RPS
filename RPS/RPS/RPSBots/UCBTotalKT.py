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
            self.children = None

        def select_move(self, t):
            r = gamma(self.counts[0] + 0.5, 1)
            p = gamma(self.counts[1] + 0.5, 1)
            s = gamma(self.counts[2] + 0.5, 1)
            scores = [s - p, r - s, p - r]
            n = r + p + s
            scores = [ucb(s, n, t) for s in scores]
            best = max(scores)
            return (best, scores.index(best))

        def update(self, h, i):
            stop = False
            for d, n in enumerate(h):
                self.counts[i] += 1
                if d >= 16 or stop:
                    return
                if self.children is None:
                    self.children = [None for _ in xrange(3)]
                if self.children[n] is None:
                    self.children[n] = MarkovTree()
                    stop = True
                self = self.children[n]

        def predict(self, h):
            path = []
            path.append(self)
            for n in h:
                if self.children is None:
                    break
                self = self.children[n]
                if self is None:
                    break
                path.append(self)
            t = sum(1.5 + sum(node.counts) for node in path)
            best_score = float("-inf")
            for n in path:
                score, move = n.select_move(t)
                if score >= best_score:
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

    tree.update(history, i)

    history.appendleft(i)
    history.appendleft(j)

node, k = tree.predict(history)
output = name[k]