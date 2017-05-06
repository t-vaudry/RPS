import random

if input == "":
    R, P, S = 0, 1, 2
    index = {"R": R, "P": P, "S": S}
    beat = ("P", "S", "R")
    counts = [[1 for _ in xrange(3)] for _ in xrange(9)]
    m = random.randrange(0, 3)
    k = None
else:
    i = index[input]
    j = index[output]
    if k is not None:
        counts[k][i] += 2
    k = 3 * i + j
    ns = counts[k]
    t = sum(ns)
    r = random.randint(0, t)
    p = 0
    for m, n in enumerate(ns):
        p += n
        if r <= p:
            break
output = beat[m]