if input == "":

    import collections
    import math
    import random

    gamma = random.gammavariate
    R, P, S = 0, 1, 2
    index = {"R": R, "P": P, "S": S}
    beat = (P, S, R)
    name = ("R", "P", "S")

    def score(probs):
        r, p, s = probs
        scores = [s - p, r - s, p - r]
        s = max(scores)
        return (s, scores.index(s))

    def score_belief(counts):
        r, p, s = counts
        r0 = s - p
        p0 = r - s
        s0 = p - r
        r1 = gamma(s + 1, 1) - gamma(p + 1, 1)
        p1 = gamma(r + 1, 1) - gamma(s + 1, 1)
        s1 = gamma(p + 1, 1) - gamma(r + 1, 1)
        scores = [r1, p1, s1]
        s = max(scores)
        return (s, scores.index(s))
        
    class MarkovTree:

        def __init__(self):
            self.counts = [0.0 for _ in xrange(3)]
            self.children = None

        def select_move(self):
            (s0, _) = score(self.counts)
            while True:
                (s1, _) = u = score_belief(self.counts)
                if s1 >= s0:
                    return u

        def update(self, h, i):
            for d, n in enumerate(h):
                if d >= 16:
                    return
                self.counts[i] += 1
                if self.children is None:
                    self.children = [MarkovTree() for _ in xrange(3)] 
                    return
                self = self.children[n]

        def predict(self, h):
            s0 = 0
            for n in h:
                s1, m1 = self.select_move()
                if s1 >= s0:
                    m = m1
                    s0 = s1
                if self.children is None:
                    return m
                self = self.children[n]

    tree = MarkovTree()
    history = collections.deque([])
    output = random.choice(name)

else:

    i = index[input]
    j = index[output]

    tree.update(history, i)

    history.appendleft(i)
    history.appendleft(j)

    output = name[tree.predict(history)]