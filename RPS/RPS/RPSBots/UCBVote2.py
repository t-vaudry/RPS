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
        return s + sqrt(2 * log(t) / n)

    def belief(xs):
        n = sum(xs)
        m = sum(1 for x in xs if x)
        if m == 0:
            a = 1.0
        else:
            a = m / (6.0 * log((n + 1.0) / m))
        return [gamma(x + a, 1) for x in xs]

    class MarkovTree:
        def __init__(self, parent = None):
            self.counts = [0.0 for _ in xrange(3)]
            self.visits = [0.0 for _ in xrange(3)]
            self.children = None
            self.parent = parent

        def select_move(self):
            r, p, s = belief(self.counts)
            visits = belief(self.visits)
            t = sum(visits) + 1.0
            n = r + p + s
            scores = [s - p, r - s, p - r]
            scores = [ucb(s / n, k, t) for s, k in zip(scores, visits)]
            best = max(scores)
            i = scores.index(best)
            self.visits[i] += 1
            return i

        def update(self, h, i):
            for n in h:
                self.counts[i] += 1
                if self.children is None:
                    break
                self = self.children[n]
                if self is None:
                    break

        def predict(self, h):
            stop = False
            d = 0
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
            leaf = self
            counts = [0, 0, 0]
            while self is not None:
                counts[self.select_move()] += 1
                self = self.parent
            r, p, s = counts
            scores = [r - s, p - r, s - p]
            s = max(scores)
            m = random.choice([i for i, x in enumerate(scores) if x == s])
            return (leaf, m)

    tree = MarkovTree()
    history = collections.deque([])

    node = tree

else:

    i = index[input]
    j = index[output]

    #while node is not None:
    #    node.visits[j] += 1
    #    node = node.parent
    tree.update(history, i)

    history.appendleft(i)
    history.appendleft(j)

node, k = tree.predict(history)
output = name[k]