if input == "":

    import collections
    import random
    import math

    log = math.log
    exp = math.exp
    third = 1.0 / 3

    def match_entropy(v, h0):
        h0 = -h0
        p = [third, third, third]
        k = -0.5
        error = 1
        n = 0
        while abs(error) >= 1e-14:
            try:
                p = [exp(k * vi) for vi in v]
            except OverflowError:
                return p
            t = sum(p)
            f = 1.0 / t
            p = [pi * f for pi in p]
            if any(pi == 0 for pi in p):
                return p
            n += 1
            h = [log(pi) * pi for pi in p]
            h1 = sum(h)
            dp = [0 for _ in xrange(3)]
            dt = sum(pi * vi for pi, vi in zip(p, v))
            dh = sum((log(pi) + 1) * pi * (vi - dt) for vi, pi in zip(v, p))
            if dh == 0:
                return p
            error = h1 - h0
            k = k - error / dh
        return p

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
                if stop or d >= 20:
                    return
                d += 1
                if self.children is None:
                    self.children = [None for _ in xrange(4)]
                if self.children[k] is None:
                    self.children[k] = MarkovTree()
                    stop = True
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
                child = self.children[k]
                if child is None:
                    return
                self = child

        def predict(self, h, n0=None):
            if n0 is None:
                n0 = [0, 0, 0]
            self.predict_helper(h, 0, n0)
            return n0

    R, P, S = 0, 1, 2
    index = {"R": R, "P": P, "S": S}
    name = ("R", "P", "S")
    beat = (P, S, R)

    both = MarkovTree()
    us = MarkovTree()
    them = MarkovTree()

    history = collections.deque([])
    our_history = collections.deque([])
    their_history = collections.deque([])

else:

    i = index[input]
    j = index[output]

    both.update(history, i)
    us.update(our_history, i)
    them.update(their_history, i)
    history.appendleft(i)
    history.appendleft(j)
    their_history.appendleft(j)
    our_history.appendleft(i)

counts = both.predict(history)
us.predict(our_history, counts)
them.predict(their_history, counts)
t = sum(counts)
probs = [(n + 3.0) / (t + 9.0) for n in counts]
r, p, s = probs
scores = [-(s - p), -(r - s), -(p - r)]
h = -sum(pi * log(pi) for pi in probs)
ps = match_entropy(scores, h)
r = random.uniform(0, sum(ps))
x = 0
for i in xrange(3):
    x += ps[i]
    if r <= x:
        break
output = name[i]