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
    beat = ("P", "S", "R")

    l = 5

    nodes = [[MarkovChain() for _ in xrange(3)] for _ in xrange(l)]

    for i in xrange(l):
        children = nodes[(i + 1) % l]
        for j in xrange(3):
            nodes[i][j].children = children

    model = MarkovChain()
    model.children = nodes[0]

    iocane = [[4.0, 0.0],
              [0.0, 0.0],
              [0.0, 0.0]]

    strategy = [["P", "S", "R"],
                ["S", "R", "P"],
                ["R", "P", "S"]]
else:
    i = index[input]
    if previous_output == beat[i]:
        iocane[strat][0] += 1
        iocane[(strat + 1) % 3][1] += 1
    elif beat[index[previous_output]] == input:
        iocane[strat][1] += 1
        iocane[(strat + 2) % 3][0] += 1
    else:
        iocane[(strat + 1) % 3][0] += 1
        iocane[(strat + 2) % 3][1] += 1
    for x in iocane:
        x[0] *= 0.99
        x[1] *= 0.99
    j = index[output]
    model = model.transition(i)
    model = model.transition(j)
counts = model.counts
t = sum(counts)
r = random.uniform(0, t)
x = 0
for i, p in enumerate(counts):
    x += p
    if r <= x:
        e = float("-inf")
        for j, (win, loss) in enumerate(iocane):
            expected_value = win - loss
            if expected_value >= e:
                e = expected_value
                strat = j
        output = strategy[strat][i]
        break
previous_output = output