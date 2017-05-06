import random

game = ["R","P","S"]

if input=="":
  history = list()
  nRock=0
  nPaper=0
  nScissor=0
  guess = list()
  output = random.choice(game)
  
else:
  history.append(input)
  nRock=history.count("R")
  nPaper=history.count("P")
  nScissor=history.count("S")
  
  i = -1
  try:
    while 1:
      i = [nRock,nPaper,nScissor].index(min([nRock,nPaper,nScissor]), i+1)
      guess.append(i)
  except ValueError:
    pass
    
  random = random.choice(guess)
  output = game[random]