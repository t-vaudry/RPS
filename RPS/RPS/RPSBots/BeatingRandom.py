import random

tobeat = random.choice(["R","P","S"])
if tobeat == "R":
  output = "P"
elif tobeat == "P":
  output = "S"
elif tobeat == "S":
  output = "R"