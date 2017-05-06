if input == "":

    import collections
    import random
    import math

    log = math.log
    log3 = log(3)

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
            self.log_p = 0
            self.counts = [0 for _ in xrange(3)]
            self.total = 0
            self.children = None

        def update(self, h, i, prediction=None):
            stop = False
            for d, k in enumerate(h):
                self.log_p += log((self.counts[i] + 1.0) / (self.total + 3.0))
                self.counts[i] += 1
                self.total += 1
                if stop or d >= 16:
                    return
                if self.children is None:
                    self.children = [None for _ in xrange(3)]
                if self.children[k] is None:
                    self.children[k] = MarkovTree()
                    stop = True
                self = self.children[k]

        def predict(self, h):
            n0 = [0, 0, 0]
            n = self.total
            w0 = self.log_p
            e = iter(h)
            w = 0
            while True:
                wi = math.exp(self.log_p - (n - self.total) * log3 + w0)
                w += wi
                for i, n in enumerate(self.counts):
                    n0[i] += wi * (n + 1.0) / (self.total + 3.0)
                if self.children is None:
                    break
                try:
                    k = next(e)
                except:
                    break
                child = self.children[k]
                if child is None:
                    break
                self = child
            return [n for n in n0]

    R, P, S = 0, 1, 2
    index = {"R": R, "P": P, "S": S}
    beat = (P, S, R)
    name = ("R", "P", "S")
    tree = MarkovTree()
    history = collections.deque([])
    output = random.choice(name)

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
    prediction = random.choice([i for i in xrange(3) if scores[i] == best])
    output = name[prediction]