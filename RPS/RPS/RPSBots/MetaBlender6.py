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
        def __init__(self):
            self.counts = [0 for _ in xrange(3)]
            self.children = None

        def update(self, h, i):
            stop = False
            for d, k in enumerate(h):
                try:
                    for j in xrange(3):
                        self.counts[j] += 2 * i[j]
                except TypeError:
                    self.counts[i] += 2
                if stop or d >= 16:
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
                if self.children is None:
                    break
                child = self.children[k]
                if child is None:
                    break
                self = child
            return n0

    R, P, S = 0, 1, 2
    index = {"R": R, "P": P, "S": S}
    beat = (P, S, R)
    name = ("R", "P", "S")
    strategies = [(R, P, S),
                  (P, S, R),
                  (S, R, P)]
    tree = MarkovTree()
    meta_tree = MarkovTree()

    history = collections.deque([])

else:

    i = index[input]
    j = index[output]

    tree.update(history, i)
    probs = [0 for _ in xrange(3)]
    f = 1.0 / sum(counts)
    for k, x in enumerate(strategies):
        for l, n in enumerate(counts):
            if x[l] == i:
                probs[k] = n * f
                break
    meta_tree.update(history, probs)
    history.appendleft(i)
    history.appendleft(j)

counts = tree.predict(history)
meta_counts = meta_tree.predict(history)
hypotheses = [None for _ in xrange(3)]
for i, _ in enumerate(hypotheses):
    x = random_index(counts)
    m = random_index(meta_counts)
    hypotheses[i] = strategies[m][x]
scores = [0, 0, 0]
for i, _ in enumerate(scores):
    for h in hypotheses:
        if i == beat[h]:
            scores[i] += 1
        elif h == beat[i]:
            scores[i] -= 1
best = max(scores)
prediction = random.choice([i for i in xrange(3) if scores[i] == best])
output = name[prediction]