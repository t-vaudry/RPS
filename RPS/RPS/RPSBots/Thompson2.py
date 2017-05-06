if input == "":

    import collections
    import random

    class MarkovTree:
        def __init__(self, counts = None):
            self.counts = [0 for _ in xrange(3)]
            self.children = None

        def update_helper(self, h, i, p, d, skips):
            stop = False
            for j in xrange(p, len(h)):
                self.counts[i] += 1
                if stop or d >= 16:
                    return
                d += 1
                k = h[j]
                if self.children is None:
                    self.children = [None for _ in xrange(4)]
                    self.children[3] = MarkovTree()
                if self.children[k] is None:
                    self.children[k] = MarkovTree()
                    stop = True
                if skips == 0:
                    self.children[3].update_helper(h, i, j + 1, d, skips + 1)
                self = self.children[k]

        def update(self, h, i):
            self.update_helper(h, i, 0, 0, 0)

        def predict_helper(self, h, p, n0):
            for j in xrange(p, len(h)):
                k = h[j]
                for i, x in enumerate(self.counts):
                    n0[i] += x
                if self.children is None:
                    return
                self.children[3].predict_helper(h, j + 1, n0)
                child = self.children[k]
                if child is None:
                    return
                self = child

        def predict(self, h):
            n0 = [0, 0, 0]
            self.predict_helper(h, 0, n0)
            return n0

    R, P, S = 0, 1, 2
    index = {"R": R, "P": P, "S": S}
    name = ("R", "P", "S")
    beat = (P, S, R)
    beaten = (S, R, P)

    tree = MarkovTree()

    history = collections.deque([])

else:

    i = index[input]
    j = index[output]

    tree.update(history, i)
    history.appendleft(i)
    history.appendleft(j)

counts = tree.predict(history)
r, p, s = [random.gammavariate(n + 2, 1) for n in counts]
scores = [s - p, r - s, p - r]
output = name[scores.index(max(scores))]