if input == "":

    import random

    class MarkovChain:
        def __init__(self, counts = None):
            self.visits = 0
            if counts is None:
                self.counts = [0 for _ in xrange(3)]
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
            self.counts[i] += 2
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

    odd = new_model(9)
    them = new_model(3)
    us = new_model(3)
    both = new_model(9)
    even = new_model(9)

    round_number = 0

else:
    round_number += 1
    i = index[input]
    j = index[output]
    both = both.transition(i, j, 0)
    them = them.transition(i, j, 1)
    us = us.transition(i, j, 2)
    if round_number % 2:
        odd = odd.transition(i, j, 2)
    else:
        even = even.transition(i, j, 2)

count_lists = [
    both.counts,
    them.counts,
    us.counts,
    odd.counts,
    even.counts
]

counts = [1 + sum(xs) for xs in zip(*count_lists)]
t = sum(counts)
r = random.randint(0, t)
x = 0
for i, p in enumerate(counts):
    x += p
    if r <= x:
        output = beat[i]
        break