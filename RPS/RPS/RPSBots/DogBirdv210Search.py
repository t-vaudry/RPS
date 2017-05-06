import random

MAX_LENGTH = 10

def leastLikely(next, inputs, inv):
  outcomes = [0, 0, 0]
  length = len(inputs)
  if (length < MAX_LENGTH):
    for x in xrange(length):
      key = inputs[x:]
      found = next.get(key, dict())
      outcomes[0] += found.get('R', 0)
      outcomes[1] += found.get('P', 0)
      outcomes[2] += found.get('S', 0)
  else:
    for x in xrange(length-MAX_LENGTH, length):
      key = inputs[x:]
      found = next.get(key, dict())
      outcomes[0] += found.get('R', 0)
      outcomes[1] += found.get('P', 0)
      outcomes[2] += found.get('S', 0)
  if inv:
    if outcomes[0] >= outcomes[1] and outcomes[0] >= outcomes[2]:
      return "R"
    if outcomes[1] >= outcomes[0] and outcomes[1] >= outcomes[2]:
      return "P"
    if outcomes[2] >= outcomes[0] and outcomes[2] >= outcomes[1]:
      return "S"
  else:
    if outcomes[0] <= outcomes[1] and outcomes[0] <= outcomes[2]:
      return "R"
    if outcomes[1] <= outcomes[0] and outcomes[1] <= outcomes[2]:
      return "P"
    if outcomes[2] <= outcomes[0] and outcomes[2] <= outcomes[1]:
      return "S"

def addToNext(next, inputs):
  length = len(inputs) - 1
  if (length < MAX_LENGTH):
    for x in xrange(length):
      key1 = inputs[x:-1]
      key2 = inputs[-1]
      found1 = next.get(key1, dict())
      found2 = found1.get(key2, 0) + 1
      found1[key2] = found2
      next[key1] = found1
  else:
    for x in xrange(length-MAX_LENGTH, length):
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
  fails = 0
else:
  oppStack += input

addToNext(oppNext, oppStack)
oppOutput = leastLikely(oppNext, oppStack, True)

addToNext(myNext, myStack)
output = leastLikely(myNext, myStack, False)

if myStack:
  if (myStack[-1] == "R" and oppStack[-1] == "P") or (myStack[-1] == "S" and oppStack[-1] == "R") or (myStack[-1] == "P" and oppStack[-1] == "S"):
    fails += 1

if random.random() < float(fails)/333:
  output = {'P': 'S', 'R': 'P', 'S':'R'}[random.choice(oppStack)]
else:
  if oppOutput == "S":
    output = random.choice((output, "R"))
  elif oppOutput == "R":
    output = random.choice((output, "P"))
  else:
    output = random.choice((output, "S"))

myStack += output