import random
game=["R","P","S"]
if input=="":
  output=random.choice(game)
else:
  if input=="R":
    output=random.choice(["S","R"])
  elif input=="P":
    output=random.choice(["R","P"])
  else:
    output=random.choice(["S","P"])