import math
import random

def action(kappa):
  p = [random.gammavariate(x+1,1) for x in kappa]
  e = [p[(i+2)%3] - p[(i+1)%3] for i in xrange(3)]
  for i in xrange(3):
    if e[i] < e[(i+1)%3] == e[(i+2)%3]:
      return random.choice([(i+1)%3,(i+2)%3])
    if e[i] <= e[(i+1)%3] < e[(i+2)%3]:
      return (i+2)%3
  return random.choice([0,1,2])

if input == '':
  hands = 'RPS'
  rhands = { 'R': 0, 'P': 1, 'S': 2 }
  stat = [[0.0 for i in xrange(3)] for j in xrange(9**2)]
  c = 0
  s = 0
else:
  c += 1
  o = rhands[input]
  if c > 2:
    stat = [[0.99 * x for x in y] for y in stat]
    stat[s][o] += 1
  s = 9 * (s % 9) + 3 * m + o
m = action(stat[s])
output = hands[m]