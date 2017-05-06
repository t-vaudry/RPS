import random
import math

def rand_dirichlet(a):
  return [random.gammavariate(x,1) for x in a]

def action(stat):
  p = rand_dirichlet([x+1 for x in stat])
  e = [p[(i+2)%3] - p[(i+1)%3] for i in xrange(3)]
  for i in xrange(3):
    if e[i] <= e[(i+1)%3] < e[(i+2)%3]:
      return (i+2)%3
    if e[i] < e[(i+1)%3] == e[(i+2)%3]:
      return random.choice([(i+1)%3,(i+2)%3])
  return random.choice([0,1,2])

if input == '':
  hands = 'RPS'
  rhands = { 'R': 0, 'P': 1, 'S': 2, '': 3 }
  stat = [[0,0,0] for i in xrange(3)]
  h = 3
  m = random.choice([0,1,2])
else:
  o = rhands[input]
  if h != 3:
    v = (o - h + 3) % 3
    stat[s][v] += 1
  s = (m - o + 3) % 3
  h = m
  m = action([stat[s][h],stat[s][(h+1)%3],stat[s][(h+2)%3]])
output = hands[m]