import random

def countBest(history):
  best = [[0, 'R'],[0, 'P'],[0, 'S']]
  for x in xrange(len(history)-1, -1, -1):
    key = history[x:]
    if len(key) > 20:
      break
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

beats = {'R': 'P', 'P': 'S', 'S': 'R'}

if not input:
  output = random.choice(('R', 'P', 'S'))
  myStack = ''
  oppStack = ''
else:
  oppStack += input
  myChoices = sorted(countBest(myStack))
  if myChoices[0][0] == myChoices[1][0] == myChoices[2][0]:
    myOutput = random.choice(('R', 'P', 'S'))
  elif myChoices[0][0] == myChoices[1][0]:
    myOutput = random.choice((myChoices[0][1], myChoices[1][1]))
  else:
    myOutput = myChoices[0][1]

  oppChoices = sorted(countBest(oppStack))
  if oppChoices[0][0] == oppChoices[1][0] == oppChoices[2][0]:
    oppOutput = random.choice(('R', 'P', 'S'))
  elif oppChoices[1][0] == oppChoices[2][0]:
    oppOutput = random.choice((beats[oppChoices[1][1]], beats[oppChoices[2][1]]))
  else:
    oppOutput = beats[oppChoices[2][1]]

  output = random.choice((myOutput, oppOutput))

myStack += output