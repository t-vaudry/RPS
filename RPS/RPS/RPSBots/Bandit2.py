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

    class MarkovTree:
        def __init__(self, counts = None):
            self.counts = [0.0 for _ in xrange(3)]
            self.visits = [0.0 for _ in xrange(3)]
            self.children = None

        def scores(self):
            r = self.counts[0]
            p = self.counts[1]
            s = self.counts[2]
            return [s - p, r - s, p - r]

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
            k = 3 * len(path)
            nu = 0.95 / k
            norm = 0
            for n in path:
                scores = n.scores()
                norm += sum(exp(nu * s) for s in scores)
            r = random.random()
            x = 0
            for n in path:
                for i, s in enumerate(n.scores()):
                    x += (0.5 * exp(nu * s)) / norm + nu
                    if x >= r:
                        return i

    tree = MarkovTree()
    history = collections.deque([])

else:

    i = index[input]
    j = index[output]

    tree.update(history, i)

    history.appendleft(i)
    history.appendleft(j)
output = name[tree.predict(history)]