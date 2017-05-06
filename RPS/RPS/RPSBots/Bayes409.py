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
  stat, s, c = [[0.0 for i in xrange(3)] for j in xrange(9**3)], 0, 0
else:
  o = {'R':0,'P':1,'S':2}[input]
  if c > 2:
    stat[s][o] = 0.9 * stat[s][o] + 1.0
  s = 9 * (s % 81) + 3 * m + o
  c += 1
m = action(stat[s])
output = 'RPS'[m]