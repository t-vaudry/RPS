import random

game = ["R","P","S"]

if input=="":
  matchHistory=[[],[]]
  countHim = [0,0,0]
  countMe = [0,0,0]
  matchNumber=0
  output = random.choice(game)
  matchHistory[0].append(game.index(output))
  
else:
  ++matchNumber
  matchHistory[1].append(game.index(input))
  if matchNumber<100:
    output=random.choice(game)
  else:
    countMe=[matchHistory[0].count("R"),matchHistory[0].count("P"),matchHistory[0].count("S")]
    countHim=[matchHistory[1].count("R"),matchHistory[1].count("P"),matchHistory[1].count("S")]
    
    output = game[(countHim.index(max(countHim))+1)%3]
    
    
  matchHistory[0].append(game.index(output))