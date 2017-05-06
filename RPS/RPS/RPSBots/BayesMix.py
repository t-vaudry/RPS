import random
import math

def model_evidence(stat, lg):
  c0 = lg[3] - 3.0 * lg[1]
  return len(stat) * c0 - sum([lg[sum(y)+3] - sum([lg[x+1] for x in y]) for y in stat])

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
  lg = [0.0] * 1010
  for i in xrange(2,1010):
    lg[i] = lg[i-1] + math.log(i-1)
  hands = 'RPS'
  rhands = { 'R': 0, 'P': 1, 'S': 2 }
  stat = [[[0,0,0] for i in xrange(9**n)] for n in xrange(4)]
  c, s = 0, 0
else:
  c += 1
  o = rhands[input]
  for n in xrange(min(4,c)):
    stat[n][s%(9**n)][o] += 1
  s = 9 * (s % 81) + 3 * m + o
ei, em = 0, model_evidence(stat[0], lg)
for n in xrange(1,3):
  e = model_evidence(stat[n], lg)
  if e > em:
    ei, em = n, e
m = action(stat[ei][s%(9**ei)])
output = hands[m]