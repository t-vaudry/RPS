import random
if input == "":
  history = ""
  output = random.choice(["R","P","S"])
else:
  history += input
  tobeat = history[random.randint(0, len(input)-1)]
  if tobeat == "R":
	output = "P"
  elif tobeat == "P":
	output = "S"
  elif tobeat == "S":
	output = "R"