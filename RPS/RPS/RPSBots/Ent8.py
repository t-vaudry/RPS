if input == "":

    import collections
    import random
    import math

    exp = math.exp
    log = math.log
    third = 1.0 / 3
    expected_entropy = -log(third)
    gamma = random.gammavariate

    def match_entropy(v, h0):
        h0 = -h0
        p = [third, third, third]
        k0 = -0.05
        k = k0
        error = 1
        n = 0
        while abs(error) >= 0.0001 * -h0:
            if n >= 9:
                break
            n += 1
            p = [exp(k * vi) for vi in v]
            t = sum(p)
            f = 1.0 / t
            p = [pi * f for pi in p]
            if any(x == 0 for x in p):
                return p
            h = [log(pi) * pi for pi in p]
            h1 = sum(h)
            dh = sum((log(pi) + 1) * vi * pi for vi, pi in zip(v, p))
            if dh == 0:
                return p
            error = h1 - h0
            k = k - error / dh
        return p

    class MarkovTree:
        def __init__(self):
            self.them = [0 for _ in xrange(3)]
            self.children = None

        def update(self, h, i, j):
            stop = False
            for d, k in enumerate(h):
                self.them[i] += 1
                if stop or d >= 16:
                    return
                if self.children is None:
                    self.children = [None for _ in xrange(3)]
                if self.children[k] is None:
                    self.children[k] = MarkovTree()
                    stop = True
                    return
                self = self.children[k]

        def predict(self, h):
            best_score = float("-inf")
            counts = [0, 0, 0]
            probs = [third, third, third]
            for i, k in enumerate(h):
                ps = [gamma(n + 1.0, 1) for n in self.them]
                f = 1.0 / sum(ps)
                r, p, s = ps
                score = max([s - p, r - s, p - r])
                if score >= best_score:
                    best_score = score
                    counts = self.them
                if self.children is None:
                    break
                child = self.children[k]
                if child is None:
                    break
                self = child
            return counts
    R, P, S = 0, 1, 2
    index = {"R": R, "P": P, "S": S}
    name = ("R", "P", "S")
    tree = MarkovTree()
    history = collections.deque([])
    epoch = 1.0

else:

    i = index[input]
    j = index[output]

    tree.update(history, i, j)
    history.appendleft(i)
    history.appendleft(j)
them = tree.predict(history)
r, p, s = [n + 1.0 for n in them]
u = 1.0 / (r + p + s)
scores = [-(s - p) * u, -(r - s) * u, -(p - r) * u]
them = [n + 7.0 for n in them]
u = 1.0 / sum(them)
p = [x * u for x in them]
h_them = -sum(pi * log(pi) for pi in p)
ps = match_entropy(scores, h_them)
r = random.random()
x = 0
for i in xrange(3):
    x += ps[i]
    if r <= x:
        break
output = name[i]