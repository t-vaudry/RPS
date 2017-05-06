import random
if input == "":
  output = random.choice(["R","P","S"])
else:
  tobeat = input[random.randint(0, len(input)-1)]
  if tobeat == "R":
	output = "P"
  elif tobeat == "P":
	output = "S"
  elif tobeat == "S":
	output = "R"