import random
def fight(a, b):
	return (a == "R" and b == "S") or (a == "S" and b == "P") or (a == "P" and b == "R")

if input == "": # initialize variables for the first round
	output = prevOutput = "R"
else:
	if fight(input, prevOutput):
		output = prevOutput = random.choice(["R","P","S"])
	if input == "R":
		output = prevOutput = "S"
	elif input == "P":
		output = prevOutput = "R"
	elif input == "S":
		output = prevOutput = "P"