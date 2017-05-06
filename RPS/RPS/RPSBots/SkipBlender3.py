if input == "":

    import collections
    import random

    def random_index(ps):
        t = sum(ps)
        r = random.uniform(0, t)
        x = 0
        for i, p in enumerate(ps):
            x += p
            if r <= x:
                break
        return i

    class MarkovTree:
        def __init__(self, counts = None):
            self.counts = [0 for _ in xrange(3)]
            self.children = None

        def update_helper(self, h, i, p, d, skips):
            stop = False
            for j in xrange(p, len(h)):
                k = h[j]
                self.counts[i] += 1
                if stop or d >= 11 or (skips >= 1 and d >= 5) or skips >= 3:
                    return
                d += 1
                if self.children is None:
                    self.children = [None for _ in xrange(4)]
                    self.children[3] = MarkovTree()
                if self.children[k] is None:
                    self.children[k] = MarkovTree()
                    stop = True
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
            n0 = [1, 1, 1]
            self.predict_helper(h, 0, n0)
            return n0

    R, P, S = 0, 1, 2
    index = {"R": R, "P": P, "S": S}
    name = ("R", "P", "S")
    beat = (P, S, R)

    tree = MarkovTree()

    history = collections.deque([])

else:

    i = index[input]
    j = index[output]

    tree.update(history, i)
    history.appendleft(i)
    history.appendleft(j)

counts = tree.predict(history)
hypotheses = [random_index(counts) for _ in xrange(3)]
scores = [0, 0, 0]
for i, _ in enumerate(scores):
    for h in hypotheses:
        if i == beat[h]:
            scores[i] += 1
        elif h == beat[i]:
            scores[i] -= 1
best = max(scores)
m = random.choice([i for i in xrange(3) if scores[i] == best])
output = name[m]