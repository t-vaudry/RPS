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

    class MarkovTree:
        def __init__(self, counts = None):
            self.counts = [0.0 for _ in xrange(3)]
            self.children = None

        def scores(self):
            r = gamma(self.counts[0] + 0.5, 1)
            p = gamma(self.counts[1] + 0.5, 1)
            s = gamma(self.counts[2] + 0.5, 1)
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
            scores = [0, 0, 0]
            for n in h:
                for i, s in enumerate(self.scores()):
                    scores[i] += s
                if self.children is None:
                    break
                self = self.children[n]
                if self is None:
                    break
            return scores.index(max(scores))
    tree = MarkovTree()
    history = collections.deque([])

    node = tree

else:

    i = index[input]
    j = index[output]

    tree.update(history, i)

    history.appendleft(i)
    history.appendleft(j)

k = tree.predict(history)
output = name[k]