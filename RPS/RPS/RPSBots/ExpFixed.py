if input == "":

    import collections
    import random
    import math

    log = math.log
    exp = math.exp
    log3 = log(3)

    def log_add(x, y):
        if y > x:
            x, y = y, x
        d = y - x
        if d < -60:
            return x
        return x + log(1.0 + exp(d))

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
            w = -n * log3
            weights = [w]
            estimators = [[1, 1, 1]]
            for d, k in enumerate(h):
                wi = self.log_p - (n + 3 * d - self.total) * log3
                w = log_add(w, wi)
                weights.append(wi)
                estimators.append(self.counts)
                if self.children is None:
                    break
                child = self.children[k]
                if child is None:
                    break
                self = child
                d += 1
            for wi, counts in zip(weights, estimators):
                for i, n in enumerate(counts):
                    n0[i] += exp(wi - w) * ((n + 0.5) / (sum(counts) + 1.5))
            return n0

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