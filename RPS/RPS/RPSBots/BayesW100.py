import random
import math

def action(stat):
  p = [random.gammavariate(x+1,1) for x in stat]
  e = [p[(i+2)%3] - p[(i+1)%3] for i in xrange(3)]
  for i in xrange(3):
    if e[i] <= e[(i+1)%3] < e[(i+2)%3]:
      return (i+2)%3
    if e[i] < e[(i+1)%3] == e[(i+2)%3]:
      return random.choice([(i+1)%3,(i+2)%3])
  return random.choice([0,1,2])

if input == '':
  hands = 'RPS'
  rhands = { 'R': 0, 'P': 1, 'S': 2 }
  stat = [[0,0,0] for i in xrange(3)]
  c = 0
  hist = []
  m = random.choice([0,1,2])
else:
  o = rhands[input]
  c += 1
  if c > 1:
    r = (o - pre + 3) % 3
    stat[s][r] += 1
    hist.append((s, r))
  if c > 101:
    s0, r0 = hist[0]
    stat[s0][r0] -= 1
    del hist[0]
  s, pre = (m - o + 3) % 3, m
  tmp = [0,0,0]
  tmp[(m+0)%3] = stat[s][0]
  tmp[(m+1)%3] = stat[s][1]
  tmp[(m+2)%3] = stat[s][2]
  m = action(tmp)
output = hands[m]