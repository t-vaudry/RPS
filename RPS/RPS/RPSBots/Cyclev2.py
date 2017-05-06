if input == "":
  oppStack = ""
  myStack = ""
  cycle = [0,  0,  0]
else:
  oppStack += input

countOppRock = oppStack.count('R')
countOppPaper = oppStack.count('P')
countOppScissor = oppStack.count('S')

if countOppPaper >= countOppRock and countOppPaper >= countOppScissor:
  output = 'S'
elif countOppScissor >= countOppRock and countOppScissor >= countOppPaper:
  output = 'R'
else:
  output = 'P'

# Win, draw, lose
if myStack and oppStack:
  if (myStack[-1] == 'R' and oppStack[-1] == 'S') or (myStack[-1] == 'P' and oppStack[-1] == 'R') or (myStack[-1] == 'S' and oppStack[-1] == 'P'):
    cycle[0] += 1
  elif (myStack[-1] == 'R' and oppStack[-1] == 'R') or (myStack[-1] == 'P' and oppStack[-1] == 'P') or (myStack[-1] == 'S' and oppStack[-1] == 'S'):
    cycle[1] += 1
  else:
    cycle[2] += 1


myStack += output

if cycle[1] >= cycle[0] and cycle[1] >= cycle[2]:
  output = {'R': 'P', 'P': 'S', 'S': 'R'}[output]
elif cycle[2] >= cycle[0] and cycle[2] >= cycle[1]:
  output = {'R': 'S', 'P': 'R', 'S': 'P'}[output]