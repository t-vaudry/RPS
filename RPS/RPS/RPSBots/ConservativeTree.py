if input == "":

    import collections
    import random

    class MarkovTree:
        def __init__(self, counts = None):
            self.counts = [0 for _ in xrange(3)]
            self.children = None

        def update(self, h, i):
            stop = False
            for d, k in enumerate(h):
                self.counts[i] += 1
                if stop or d >= 128:
                    return
                if self.children is None:
                    self.children = [None for _ in xrange(3)]
                if self.children[k] is None:
                    self.children[k] = MarkovTree()
                    stop = True
                self = self.children[k]

        def predict(self, h):
            n0 = [0, 0, 0]
            for d, k in enumerate(h):
                for i, x in enumerate(self.counts):
                    n0[i] += x
                if self.children is None:
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

observations = sum(tree.counts)
t = sum(counts)
if t != 0:
    u = observations / float(t)
    normalized_counts = [x * u + 0.5 for x in counts]
    r = random.uniform(0, sum(normalized_counts))
    x = 0
    for i, p in enumerate(counts):
        x += p
        if r <= x:
            break
else:
    i = random.randrange(0, 3)
output = beat[i]