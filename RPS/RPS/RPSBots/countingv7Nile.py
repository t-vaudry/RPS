import random

game = ["R","P","S"]

if input=="":
  matchHistory=[[],[]]
  countHim = [0,0,0]
  matchNumber=0
  output = random.choice(game)
  
else:
  ++matchNumber
  matchHistory[1].append(game.index(input))
  if matchNumber<100:
    output=random.choice(game)
  else:
    countHim=[matchHistory[1].count(0),matchHistory[1].count(1),matchHistory[1].count(2)]
    if (float(max(countHim))/matchNumber)<.37:
      output=random.choice(game)
    else:
      if matchHistory[1][matchNumber-1]==matchHistory[1][matchNumber-2]==matchHistory[1][matchNumber-3]:
        output = game[(matchHistory[1][matchNumber-1]+1)%3]
      else:
        output = game[(countHim.index(max(countHim))+1)%3]
  
matchHistory[0].append(game.index(output))