if input == "":

    import random

    class MarkovChain:
        def __init__(self, counts = None):
            self.visits = 0
            if counts is None:
                self.counts = [3, 3, 3]
            else:
                self.counts = counts
            self.children = [self, self, self]

        def split_edge(self, i):
            old = self.children[i]
            new = MarkovChain(old.counts)
            self.children[i] = new
            new.children = old.children

        def unnormalized_probabilities(self):
            return [n + 0 for n in self.counts]

        def transition(self, i):
            self.visits += 1
            self.counts[i] += 1
            for i in xrange(3):
                self.counts[i] *= 0.99
            if self.children[i].visits >= 8:
                self.split_edge(i)
            return self.children[i]

    R, P, S = 0, 1, 2
    index = {"R": R, "P": P, "S": S}
    names = ("R", "P", "S")
    beat = (P, S, R)
    namebeat = ("P", "S", "R")

    rel = {}
    for i in xrange(3):
        for j in xrange(3):
            a = names[i]
            b = names[j]
            if beat[i] == j:
                rel[(a, b)] = 0
            elif beat[j] == i:
                rel[(a, b)] = 2
            else:
                rel[(a, b)] = 1

    unrel = {}
    for i in xrange(3):
        for j in xrange(3):
            a = names[i]
            if j == 1:
                unrel[(a, j)] = i
            elif j == 0:
                unrel[(a, j)] = beat[i]
            else:
                unrel[(a, j)] = beat[beat[i]]

    r0 = MarkovChain()
    p0 = MarkovChain()
    s0 = MarkovChain()
    r1 = MarkovChain()
    p1 = MarkovChain()
    s1 = MarkovChain()
    r2 = MarkovChain()
    p2 = MarkovChain()
    s2 = MarkovChain()
    children0 = [r0, p0, s0]
    children1 = [r1, p1, s1]
    children2 = [r2, p2, s2]
    for c in children0:
        c.children = children1
    for c in children1:
        c.children = children2
    for c in children2:
        c.children = children0
    model = MarkovChain()
    model.children = children0
    output = random.choice(names)
else:
    i = rel[(prev_output, input)]
    j = rel[(input, output)]
    model = model.transition(i)
    model = model.transition(j)
    counts = model.unnormalized_probabilities()
    t = sum(counts)
    r = random.uniform(0, t)
    x = 0
    for k, p in enumerate(counts):
        x += p
        if r <= x:
            output = namebeat[unrel[(output, k)]]
            break
prev_output = output