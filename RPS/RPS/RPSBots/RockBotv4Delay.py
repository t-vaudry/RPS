import random

def leastLikely(next, inputs, inv):
  outcomes = [0, 0, 0]
  length = len(inputs)
  if (length < 30):
    if inv:
      return "R"
    else:
      return "P"
  else:
    for x in xrange(length-30, length):
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
  if (length < 30):
    for x in xrange(length):
      key1 = inputs[x:-1]
      key2 = inputs[-1]
      found1 = next.get(key1, dict())
      found2 = found1.get(key2, 0) + 1
      found1[key2] = found2
      next[key1] = found1
  else:
    for x in xrange(length-30, length):
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
oppOutput = leastLikely(oppNext, oppStack, True)

addToNext(myNext, myStack)
output = leastLikely(myNext, myStack, False)

if oppOutput == "S":
  output = random.choice((output, "R"))
elif oppOutput == "R":
  output = random.choice((output, "P"))
else:
  output = random.choice((output, "S"))

myStack += output