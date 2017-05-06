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
        while abs(error) >= 0.00000001 * -h0:
            if k < -20:
                return p
            p = [exp(k * vi) for vi in v]
            t = sum(p)
            f = 1.0 / t
            p = [pi * f for pi in p]
            h = [log(pi) * pi for pi in p]
            h1 = sum(h)
            dh = sum((log(pi) + 1) * vi * pi for vi, pi in zip(v, p))
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
        def __init__(self, us=None, them=None):
            self.entropy = 0
            self.total = 0
            if us is None:
                self.us = [0 for _ in xrange(3)]
            else:
                self.us = list(us)
            if them is None:
                self.them = [0 for _ in xrange(3)]
            else:
                self.them = list(them)
            self.children = None

        def update(self, h, i, j):
            stop = False
            for k in h:
                p_them = (self.them[i] + 0.5) / (self.total + 1.5)
                p_us = (self.us[i] + 0.5) / (self.total + 1.5)
                self.entropy -= log(p_them)
                self.them[i] += 1
                self.us[j] += 1
                self.total += 1
                if self.children is None:
                    self.children = [None for _ in xrange(3)]
                if self.children[k] is None:
                    self.children[k] = MarkovTree(self.us, self.them)
                    return
                self = self.children[k]

        def predict(self, h):
            us = [1, 1, 1]
            them = [1, 1, 1]
            entropy = float("inf")
            t = 0.0
            for i, k in enumerate(h):
                entropy += self.entropy
                t += self.total
                for i in xrange(3):
                    us[i] += self.us[i]
                    them[i] += self.them[i]
                if self.children is None:
                    break
                child = self.children[k]
                if child is None:
                    break
                self = child
            return (us, them, entropy / (t + 1.0))

    R, P, S = 0, 1, 2
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

us, them, h_them = tree.predict(history)
them = [gamma(n + 1, 1) for n in them]
r, p, s = them
scores = [-(s - p), -(r - s), -(p - r)]
if h_them < 0:
    scores = [-s for s in scores]
    h_them = -h_them
delta = h_them - expected_entropy
h = expected_entropy + delta
ps = match_entropy(scores, h)
output = name[random_index(ps)]