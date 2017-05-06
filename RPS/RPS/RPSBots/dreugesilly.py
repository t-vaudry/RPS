from random import choice, random
from collections import defaultdict

options = ['R', 'P', 'S']
better = ['P', 'S', 'R']
indices = {'R':0, 'P':1, 'S':2}
opts = indices.items()

if input == '':
    prevstate = choice(options)
    input = choice(options)

counts = defaultdict(lambda: defaultdict(lambda: [10, 10, 10]))

counthist = counts[prevstate][input]

denom = sum(counthist)
item = choice(opts)
if (float(counthist[item[1]]) / denom >= random()):
    output = better[item[1]]
else:
    output = item[0]

counts[prevstate][input][indices[output]] += 1

prevstate = output