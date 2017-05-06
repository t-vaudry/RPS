if input == "":

    import collections
    import math
    import random

    gamma = random.gammavariate
    sqrt = math.sqrt
    log = math.log
    exp = math.exp
    R, P, S = 0, 1, 2
    index = {"R": R, "P": P, "S": S}
    beat = (P, S, R)
    name = ("R", "P", "S")
    third = 1.0 / 3.0

    def psi(k, x):
        u = (1.0 / k) * math.pow((2.5 * sqrt(1000 * k) / (-x)), 1.5)
        return u

    def phi(c, scores, k):
        return sum(psi(k, s - c) for s in scores)

    def dpsi(k, x):
        return -(1054.39) / (x * x * x * sqrt(-sqrt(k) / x))

    def dphi(c, scores, k):
        return -sum(dpsi(k, s - c) for s in scores)

    class MarkovTree:
        def __init__(self, counts = None):
            self.counts = [0.0 for _ in xrange(3)]
            self.visits = [0.0 for _ in xrange(3)]
            self.probs = [0.0 for _ in xrange(3)]
            self.children = None

        def scores(self):
            counts = [gamma(x + 0.5, 1) for x in self.counts]
            r, p, s = self.counts
            return [s - p, r - s, p - r]

        def update(self, h, i):
            stop = False
            leaf = False
            for d, n in enumerate(h):
                self.counts[i] += 1
                if stop or d >= 64:
                    return
                if self.children is None:
                    leaf = True
                    self.children = [None for _ in xrange(3)]
                if self.children[n] is None:
                    self.children[n] = MarkovTree()
                    stop = True
                self = self.children[n]

        def predict(self, h):
            scores = []
            scores.extend(self.scores())
            for n in h:
                if self.children is None:
                    break
                if self.children[n] is None:
                    break
                self = self.children[n]
                scores.extend(self.scores())
            c0 = 360.0
            c = c0
            best = max(scores)
            phi0 = 0
            k = len(scores)
            while True:
                if c <= best:
                    c = best + 1
                phi0 = phi(c, scores, k)
                c = c - (phi0 - 1.0) / dphi(c, scores, k)
                if abs(phi0 - 1) < 0.000001:
                    break
            r = random.random()
            x = 0
            for i, s in enumerate(scores):
                x += psi(k, s - c)
                if r <= x:
                    return i % 3

    tree = MarkovTree()
    history = collections.deque([])
    epoch = 1
    v = 2.0 / 3
else:

    epoch += 1
    i = index[input]
    j = index[output]

    tree.update(history, i)

    history.appendleft(i)
    history.appendleft(j)
output = name[tree.predict(history)]