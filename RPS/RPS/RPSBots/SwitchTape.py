if input == "":

    import math
    import random

    class MarkovChain:
        def __init__(self, counts = None):
            self.visits = 0
            if counts is None:
                self.counts = [1 for _ in xrange(3)]
            else:
                self.counts = counts
            self.children = None

        def split_edge(self, i):
            old = self.children[i]
            new = MarkovChain(old.counts)
            self.children[i] = new
            new.children = old.children

        def transition(self, i, j, t):
            self.visits += 1
            self.counts[i] += 1
            if t == 0:
                k = 3 * i + j
            elif t == 1:
                k = i
            else:
                k = j
            if self.children[k].visits >= 2:
                self.split_edge(k)
            return self.children[k]

    R, P, S = 0, 1, 2
    index = {"R": R, "P": P, "S": S}
    beat = ("P", "S", "R")

    l = 3

    def new_model(n):
        nodes = [[MarkovChain() for _ in xrange(n)] for _ in xrange(l)]
        for i in xrange(l):
            children = nodes[(i + 1) % l]
            for j in xrange(n):
                nodes[i][j].children = children
        model = MarkovChain()
        model.children = nodes[0]
        return model

    def log(x):
        if x < 0.0:
            for i in xrange(100):
                print(x)
        return math.log(x)

    gamma = random.gammavariate

    def random_expectation(x):
        nr = gamma(x[0], 1)
        np = gamma(x[1], 1)
        ns = gamma(x[2], 1)
        t  = nr + np + ns
        return (nr * (nr - ns) + np * (np - nr) + ns * (ns - np)) / t * t

    def clamp(x):
        if x <= 0.0:
            return 0.0
        else:
            return x

    both = new_model(9)
    them = new_model(3)
    us = new_model(3)

else:
    i = index[input]
    j = index[output]
    both = both.transition(i, j, 0)
    them = them.transition(i, j, 1)
    us = us.transition(i, j, 2)

counts = [both.counts, them.counts, us.counts]
best_score = float("-inf")
for x in counts:
    score = random_expectation(x)
    if score >= best_score:
        best_score = score
        best = x
t = sum(best)
r = random.randint(0, t)
x = 0
for i, p in enumerate(best):
    x += p
    if r <= x:
        output = beat[i]
        break