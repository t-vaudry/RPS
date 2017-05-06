import random

game=["R","P","S"]

if input=="":
  myHistory=list()
  hisHistory=list()
  output=random.choice(game)
  
else:
  hisHistory.append(input)
  output=random.choice(game)
  if len(hisHistory)>100:
    decisionMatrix=[myHistory[len(myHistory)-3],myHistory[len(myHistory)-2],myHistory[len(myHistory)-1]]
    for i in range(len(myHistory)-5):
      if([myHistory[i],myHistory[i+1],myHistory[i+2]]==decisionMatrix):
        output=game[game.index(hisHistory[i+3])]
        break
        
myHistory.append(output)