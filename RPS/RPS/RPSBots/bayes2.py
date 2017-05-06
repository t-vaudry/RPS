import random
import math

def rand_dirichlet(a):
  p = [random.gammavariate(x,1) for x in a]
  s = sum(p)
  return [x / s for x in p]

def action():
  p = rand_dirichlet([x+1 for x in stat[prev[0]]])
  e = [p[(i+1)%3] - p[(i+2)%3] for i in xrange(3)]
  for i in xrange(3):
    if e[i] < e[(i+1)%3] == e[(i+2)%3]:
      return random.choice([(i+1)%3,(i+2)%3])
    if e[i] <= e[(i+1)%3] < e[(i+2)%3]:
      return (i+2)%3
  return random.choice([0,1,2])

def result(mine, others):
  stat[prev[0]][others] += 1
  prev[0] = 3 * mine + others

if input == '':
  hands = 'RPS'
  rhands = { 'R': 0, 'P': 1, 'S': 2 }
  stat = [[0,0,0] for i in xrange(10)]
  prev = [9]
else:
  result(old_mine, rhands[input])
old_mine = action()
output = hands[old_mine]