import random

MAX_MARKOV = 40

def guessedProb(next, inputs):
  outcomes = [0, 0, 0]
  length = len(inputs)
  if (length < MAX_MARKOV):
    for x in xrange(length):
      key = inputs[x:]
      found = next.get(key, dict())
      outcomes[0] += found.get('R', 0)
      outcomes[1] += found.get('P', 0)
      outcomes[2] += found.get('S', 0)
  else:
    for x in xrange(length-MAX_MARKOV, length):
      key = inputs[x:]
      found = next.get(key, dict())
      outcomes[0] += found.get('R', 0)
      outcomes[1] += found.get('P', 0)
      outcomes[2] += found.get('S', 0)
  return outcomes

def addToNext(next, inputs):
  length = len(inputs) - 1
  if (length < MAX_MARKOV):
    for x in xrange(length):
      key1 = inputs[x:-1]
      key2 = inputs[-1]
      found1 = next.get(key1, dict())
      found2 = found1.get(key2, 0) + 1
      found1[key2] = found2
      next[key1] = found1
  else:
    for x in xrange(length-MAX_MARKOV, length):
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
else:
  oppStack += input

addToNext(oppNext, oppStack)
oppGuess = guessedProb(oppNext, oppStack)
addToNext(myNext, myStack)
myGuess = guessedProb(myNext, myStack)

totalSum = sum(myGuess) + sum(oppGuess)
if totalSum:
  guess = random.randint(0, totalSum - 1)
  rockCutoff = myGuess[0] + oppGuess[2]
  paperCutoff = rockCutoff + myGuess[1] + oppGuess[0]

  if guess < rockCutoff:
    output = "R"
  elif guess < paperCutoff:
    output = "P"
  else:
    output = "S"
else:
  output = "P"

myStack += output