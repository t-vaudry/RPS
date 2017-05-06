import math
import random

def action(kappa):
    p = [random.gammavariate(x+1.0,1.0) for x in kappa]
    e = [p[(i+2)%3] - p[(i+1)%3] for i in xrange(3)]
    for i in xrange(3):
        if e[i] < e[(i+1)%3] == e[(i+2)%3]:
            return random.choice([(i+1)%3,(i+2)%3])
        if e[i] <= e[(i+1)%3] < e[(i+2)%3]:
            return (i+2)%3
    return random.choice([0,1,2])

if input == '':
    c, stat = 0, [[0.0 for i in xrange(3)] for j in xrange(4)]
else:
    o = {'R':0, 'P':1, 'S':2 }[input]
    c += 1
    if c > 1:
        for i in xrange(3):
            for j in xrange(3):
                stat[i][j] *= 0.99
        stat[s][(o-p+3)%3] += 1.0
    s, p = (m - o + 3) % 3, m
    for i in xrange(3):
        stat[-1][(p+i)%3] = stat[s][i]    
m = action(stat[-1])
output = 'RPS'[m]