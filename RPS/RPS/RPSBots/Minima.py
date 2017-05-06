import random

if input == "":
    beat = {"R": "P", "P": "S", "S": "R"}
    counts = {"R": 1, "P": 1, "S": 1}
else:
    counts[input] += 2
t = sum(counts.values())
r = random.randint(0, t)
p = 0
for s, n in counts.iteritems():
    p += n
    if r <= p:
        break
output = beat[s]