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
        while abs(error) >= 0.0001 * -h0:
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
            them = [0.0, 0.0, 0.0]
            for i, k in enumerate(h):
                for i in xrange(3):
                    them[i] += self.them[i]
                if self.children is None:
                    break
                child = self.children[k]
                if child is None:
                    break
                self = child
            return them
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
them = [n + 15.0 for n in them]
t = sum(them)
p_them = [x / t for x in them]
h_them = -sum(pi * log(pi) for pi in p_them)
r, p, s = them
u = t + 1.0
scores = [-(s - p) / u, -(r - s) / u, -(p - r) / u]
delta = expected_entropy - h_them
h = expected_entropy - delta * (1 - 1.0 / epoch)
ps = match_entropy(scores, h)
output = name[random_index(ps)]
epoch += 1.0