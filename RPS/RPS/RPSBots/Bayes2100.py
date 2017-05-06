import random
import math

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
  stat = [[0,0,0] for i in xrange(9)]
  hist = []
  s = -1
  m = random.choice([0,1,2])
else:
  o = rhands[input]
  if s == -1:
    s = 3 * m + o
    m = random.choice([0,1,2])
  else:
    hist.append((s, o))
    stat[s][o] += 1
    if len(hist) > 100:
      stat[hist[0][0]][hist[0][1]] -= 1
      del hist[0]
    s = 3 * m + o
    m = action(stat[s])
output = hands[m]