import random

def iWon(me, them):
  if me == "S":
    if them == "P":
      return 1
    elif them == "R":
      return -1
  elif me == "P":
    if them == "R":
      return 1
    elif them == "S":
      return -1
  elif me == "R":
    if them == "S":
      return 1
    elif them == "P":
      return -1
  return 0

if input == "":
  oppStack = []
  myStack = []
  alt = False
elif input == "R":
  oppStack.append("R")
elif input == "P":
  oppStack.append("P")
elif input == "S":
  oppStack.append("S")

if sum(iWon(myStack[i], oppStack[i]) for i in xrange(len(myStack), len(myStack))) < 0:
  alt = not alt

oppRocks = oppStack.count("R")
oppPapers = oppStack.count("P")
oppScissors = oppStack.count("S")

if oppRocks > oppPapers and oppRocks > oppScissors:
  output = "P"
elif oppPapers > oppRocks and oppPapers > oppScissors:
  output = "S"
elif oppScissors > oppRocks and oppScissors > oppPapers:
  output = "R"
else:
  output = random.choice(["R","P","S"])

if alt:
  if output == "R":
    output = "S"
  elif output == "S":
    output = "P"
  else:
    output = "R"

myStack.append(output)