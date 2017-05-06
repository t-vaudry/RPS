import random
move = random.randint(0, 27)
choices = ["P", "R", "S", "P", "S", "R", "P", "R", "S", "P", "P", "P", "P", "P", "S", "P", "P", "P", "S", "P", "R", "S", "S", "S", "S", "P", "P", "R"]

if input == "":
	rock = paper = scissor = 0

if input == "R":
	rock += 1
	output = "P"
elif input == "P":
	paper += 1
	output = "S"
elif input == "S":
	scissor += 1
	output = "R"
else:
	output = 'P'

if rock > 0 and paper > 0 and scissor > 0:
	output = choices[move]