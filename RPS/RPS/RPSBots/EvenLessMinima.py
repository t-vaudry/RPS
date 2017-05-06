import random

if input == "":
    R, P, S = 0, 1, 2
    index = {"R": R, "P": P, "S": S}
    beat = ("P", "S", "R")
    name = ("R", "P", "S")
    counts = [[1 for _ in xrange(3)] for _ in xrange(9)]
    m = random.randrange(0, 3)
    k = None

    def random_index(x):
        r = random.uniform(0, sum(x))
        t = 0
        for i, p in enumerate(x):
            t += p
            if r <= t:
                break
        return i
            
else:
    i = index[input]
    j = index[output]
    if k is not None:
        counts[k][i] += 2
    k = 3 * i + j
    ns = counts[k]

    hypotheses = [random_index(ns) for _ in xrange(3)]
    scores = [0, 0, 0]
    for i, _ in enumerate(scores):
        for h in hypotheses:
            if i == beat[h]:
                 scores[i] += 1
            elif h == beat[i]:
                 scores[i] -= 1
    best = max(scores)
    m = random.choice([i for i, x in enumerate(scores) if x == best])

output = name[m]