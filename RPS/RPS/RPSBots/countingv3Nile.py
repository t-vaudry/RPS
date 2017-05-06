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
    countHim=[matchHistory[1].count("R"),matchHistory[1].count("P"),matchHistory[1].count("S")]
    if (max(countHim)/matchNumber)<.35:
      output=random.choice(game)
    else:
      if matchHistory[1][matchNumber-1]==matchHistory[1][matchNumber-2]:
        output = game[(matchHistory[1][matchNumber-1]+1)%3]
      else:
        output = game[(countHim.index(max(countHim))+1)%3]
  
matchHistory[0].append(game.index(output))