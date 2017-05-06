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
    third = 1.0 / 3.0

    class MarkovTree:
        def __init__(self, parent = None):
            self.counts = [0.0 for _ in xrange(3)]
            self.visits = [1.0 for _ in xrange(3)]
            self.children = None
            self.parent = parent

        def select_move(self, k):
            r = gamma(self.counts[0] + 1, 1)
            p = gamma(self.counts[1] + 1, 1)
            s = gamma(self.counts[2] + 1, 1)
            u = 1.0 / (r + p + s)
            scores = [s - p, r - s, p - r]
            for i, (s, v) in enumerate(zip(scores, self.visits)):
                scores[i] = s * u + sqrt(max(log(1000 / (3 * v)), 0) / v)
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
                    self.children[n] = MarkovTree(self)
                    stop = True
                child = self.children[n]
                self = child
                path.append(self)
            best_score = float("-inf")
            best_node = None
            k = 3 * len(path) + 1
            leaf = self
            for n in path:
                score, move = n.select_move(k)
                if score >= best_score:
                    best_score = score
                    best_node = n
                    best_move = move
            return (leaf, best_move)

    tree = MarkovTree()
    history = collections.deque([])

    node = tree

else:

    i = index[input]
    j = index[output]

    while node is not None:
        node.visits[j] += 1
        node = node.parent
    tree.update(history, i)

    history.appendleft(i)
    history.appendleft(j)

node, k = tree.predict(history)
output = name[k]