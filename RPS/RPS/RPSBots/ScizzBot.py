def iWon(me, them):
  if me == "S" and them == "P":
    return True
  elif me == "P" and them == "R":
    return True
  elif me == "R" and them == "S":
    return True

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

if len(myStack) % 5 == 0:
  if sum(iWon(myStack[i], oppStack[i]) for i in xrange(len(myStack), len(myStack))) < 3:
    alt = not alt

oppRocks = oppStack.count("R")
oppPapers = oppStack.count("P")
oppScissors = oppStack.count("S")

if oppRocks >= oppPapers and oppRocks >= oppScissors:
  output = "P"
elif oppPapers >= oppRocks and oppPapers >= oppScissors:
  output = "S"
else:
  output = "R"

if alt:
  if output == "R":
    output = "S"
  elif output == "S":
    output = "P"
  else:
    output = "R"

myStack.append(output)