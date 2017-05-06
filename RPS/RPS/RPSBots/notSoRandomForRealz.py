import random

game = ["R","P","S"]

if input=="":
  history = list()
  guess = list()
  output = random.choice(game)
  
else:
  history.append(input)
  count = [history.count("R"),history.count("P"),history.count("S")]
  
  i = -1
  try:
    while 1:
      i = count.index(min(count), i+1)
      guess.append(i)
  except ValueError:
    pass
  
  output = game[(random.choice(guess)+1)%3]