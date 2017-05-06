import random

if input == "":
	stack = []
elif input == "R":
	stack.append("R")
elif input == "P":
	stack.append("P")
elif input == "S":
	stack.append("S")

if len(stack) >= 50:
	rocks = stack.count("R")
	papers = stack.count("P")
	scissors = stack.count("S")
	if scissors < papers: 
		if scissors < rocks:
			output = "R"
		elif rocks < scissors:
			output = "P"
		else:
			output = random.choice(["R", "P", "S"])
	elif papers < rocks:
		if papers < scissors:
			output = "S"
		elif scissors < papers:
			output = "R"
		else:
			output = random.choice(["R", "P", "S"])
	elif rocks < scissors:
		if rocks < papers:
			output = "P"
		elif papers < rocks:
			output = "S"
		else:
			output = random.choice(["R", "P", "S"])
else:
	output = random.choice(["R", "P", "S"])