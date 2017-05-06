if input == "":

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

        def transition(self, i, j):
            self.visits += 1
            self.counts[i] += 1
            k = 3 * i + j
            if self.children[k].visits >= 9:
                self.split_edge(k)
            return self.children[k]

    R, P, S = 0, 1, 2
    index = {"R": R, "P": P, "S": S}
    namebeat = ("P", "S", "R")

    l = 3

    nodes = [[MarkovChain() for _ in xrange(9)] for _ in xrange(l)]

    for i in xrange(l):
        children = nodes[(i + 1) % l]
        for j in xrange(9):
            nodes[i][j].children = children

    model = MarkovChain()
    model.children = nodes[0]

else:
    i = index[input]
    j = index[output]
    model = model.transition(i, j)
counts = model.counts
t = sum(counts)
r = random.randint(0, t)
x = 0
for i, p in enumerate(counts):
    x += p
    if r <= x:
        output = namebeat[i]
        break