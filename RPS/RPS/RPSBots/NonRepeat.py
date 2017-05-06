import random

def countBest(history):
  best = [[0, 'R'],[0, 'P'],[0, 'S']]
  for x in xrange(len(history)-1, -1, -1):
    key = history[x:]
    countRock = history.count(key + 'R')
    countScissor = history.count(key + 'P')
    countPaper = history.count(key + 'S')
    if countRock + countScissor + countPaper == 0:
      break
    else:
      best[0][0] += countRock
      best[1][0] += countScissor
      best[2][0] += countPaper
  return best

if not input:
  output = 'P'
  stack = ''
else:
  choices = sorted(countBest(stack))
  if choices[0][0] == choices[1][0] == choices[2][0]:
    output = random.choice(('R', 'P', 'S'))
  elif choices[0][0] == choices[1][0]:
    output = random.choice((choices[0][1], choices[1][1]))
  else:
    output = choices[0][1]

stack += output