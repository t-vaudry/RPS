import random

MAX_LENGTH = 10

def likely(next, inputs):
  outcomes = [[0, 'R'], [0, 'P'], [0, 'S']]
  tmpInputs = inputs[-MAX_LENGTH:]
  for x in xrange(len(tmpInputs)):
    key = inputs[x:]
    found = next.get(key, dict())
    outcomes[0][0] += found.get('R', 0)
    outcomes[1][0] += found.get('P', 0)
    outcomes[2][0] += found.get('S', 0)
  return outcomes

def addToNext(next, inputs):
  length = len(inputs) - 1
  tmpInputs = inputs[-(MAX_LENGTH+1):]
  for x in xrange(len(tmpInputs) - 2):
    key1 = inputs[x:-1]
    key2 = inputs[-1]
    found1 = next.get(key1, dict())
    found2 = found1.get(key2, 0) + 1
    found1[key2] = found2
    next[key1] = found1

if input == "":
  myNext = dict()
  oppNext = dict()
  myStack = ""
  oppStack = ""
  turns = 1
  #           RR, RP, RS, PR, PP, PS, SR, SP, SS
  predictor = [0,  0,  0,  0,  0,  0,  0,  0,  0]
  oppPred = False
else:
  oppStack += input
  turns += 1

addToNext(oppNext, oppStack)
if oppPred:
  if input == 'R':
    predictor[0] += oppPred[0][0]
    predictor[1] += oppPred[1][0]
    predictor[2] += oppPred[2][0]
  elif input == 'P':
    predictor[3] += oppPred[0][0]
    predictor[4] += oppPred[1][0]
    predictor[5] += oppPred[2][0]
  else:
    predictor[6] += oppPred[0][0]
    predictor[7] += oppPred[1][0]
    predictor[8] += oppPred[2][0]
oppPred = likely(oppNext, oppStack)

addToNext(myNext, myStack)
myPred = likely(myNext, myStack)

if turns < 100:
  output = random.choice(('P', 'S', 'R'))
else:
  oppBestChoice = [[oppPred[0]*predictor[0] + oppPred[1]*predictor[3] + oppPred[2]*predictor[6], 'P'], [oppPred[0]*predictor[1] + oppPred[1]*predictor[4] + oppPred[2]*predictor[7], 'S'], [oppPred[0]*predictor[2] + oppPred[1]*predictor[5] + oppPred[2]*predictor[8], 'R']]
  output = random.choice((sorted(myPred)[0][1], sorted(oppBestChoice)[-1][1]))

myStack += output