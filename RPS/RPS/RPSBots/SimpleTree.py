if input == "":

    import collections
    import random

    class MarkovTree:
        def __init__(self, counts = None):
            self.counts = [0 for _ in xrange(3)]
            self.children = None
            self.total = 0

        def update(self, h, i):
            stop = False
            for d, k in enumerate(h):
                self.counts[i] += 2
                self.total += 2
                if stop or d >= 5:
                    return
                if self.children is None:
                    self.children = [None for _ in xrange(3)]
                if self.children[k] is None:
                    self.children[k] = MarkovTree()
                    stop = True
                self = self.children[k]

        def predict(self, h):
            n0 = [1, 1, 1]
            for d, k in enumerate(h):
                for i, x in enumerate(self.counts):
                    n0[i] += x
                if self.children is None or d >= 5:
                    break
                child = self.children[k]
                if child is None:
                    break
                self = child
            return n0

    R, P, S = 0, 1, 2
    index = {"R": R, "P": P, "S": S}
    beat = ("P", "S", "R")

    tree = MarkovTree()

    history = collections.deque([])

else:

    i = index[input]
    j = index[output]

    tree.update(history, i)
    history.appendleft(i)
    history.appendleft(j)

counts = tree.predict(history)
t = sum(counts)
r = random.uniform(0, t)
x = 0
for i, p in enumerate(counts):
    x += p
    if r <= x:
        break
output = beat[i]