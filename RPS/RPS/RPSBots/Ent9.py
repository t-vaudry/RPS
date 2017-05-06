if input == "":

    import collections
    import random
    import math

    exp = math.exp
    log = math.log
    third = 1.0 / 3
    expected_entropy = -log(third)
    gamma = random.gammavariate
    R, P, S = 0, 1, 2
    beat = (P, S, R)
    beat2 = (S, R, P)

    def match_entropy(v, h0):
        h0 = -h0
        p = [third, third, third]
        k = -0.5
        error = 1
        n = 0
        while exp(abs(error)) - 1 >= 0.00000000001:
            p = [exp(k * vi) for vi in v]
            t = sum(p)
            f = 1.0 / t
            p = [pi * f for pi in p]
            if any(x == 0 for x in p):
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

    class MarkovTree:
        def __init__(self):
            self.us = [0 for _ in xrange(3)]
            self.them = [0 for _ in xrange(3)]
            self.meta = [0 for _ in xrange(3)]
            self.children = None

        def update(self, h, i, j):
            stop = False
            for d, k in enumerate(h):
                r, p, s = self.us
                scores = [s - p, r - s, p - r]
                m = scores.index(max(scores))
                if m == i:
                    self.meta[0] += 1
                elif m == beat[i]:
                    self.meta[1] += 1
                else:
                    self.meta[2] += 1
                self.us[j] += 1
                self.them[i] += 1
                if d >= 16 or stop:
                    return
                if self.children is None:
                    self.children = [None for _ in xrange(3)]
                if self.children[k] is None:
                    self.children[k] = MarkovTree()
                    stop = True
                self = self.children[k]

        def predict(self, h):
            best_score = float("-inf")
            best_counts = [0, 0, 0]
            best_scores = [0, 0, 0]
            i = 0
            for i, k in enumerate(h):
                counts = [gamma(n + 1, 1) for n in self.them]
                f = 1.0 / sum(counts)
                r, p, s = counts
                scores = [f * (s - p), f * (r - s), f * (p - r)]
                score = max(scores)
                if score >= best_score:
                    best_score = score
                    best_counts = self.them
                    best_scores = scores
                r, p, s = self.us
                scores = [s - p, r - s, p - r]
                m = scores.index(max(scores))
                counts = [gamma(n + 1, 1) for n in self.meta]
                f = 1.0 / sum(counts)
                a, b, c = counts
                scores = [0, 0, 0]
                scores[m] = f * (c - b)
                scores[beat[m]] = f * (a - c)
                scores[beat2[m]] = f * (b - a)
                score = max(scores)
                if score >= best_score:
                    best_score = score
                    best_scores = scores
                    best_counts = self.meta
                if self.children is None:
                    break
                child = self.children[k]
                if child is None:
                    break
                self = child
            return best_counts, best_scores

    index = {"R": R, "P": P, "S": S}
    name = ("R", "P", "S")
    tree = MarkovTree()
    history = collections.deque([])

else:

    i = index[input]
    j = index[output]

    tree.update(history, i, j)
    history.appendleft(i)
    history.appendleft(j)

counts, scores = tree.predict(history)
counts = [n + 7 for n in counts]
u = 1.0 / sum(counts)
p = [x * u for x in counts]
h = -sum(pi * log(pi) for pi in p)
ps = match_entropy([-x for x in scores], h)
h1 = -sum(pi * log(pi) for pi in ps)
r = random.uniform(0, sum(ps))
x = 0
for i in xrange(3):
    x += ps[i]
    if r <= x:
        break
output = name[i]