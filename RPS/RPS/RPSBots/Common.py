import random

if input == "": # initialize variables for the first round
	moves = []
	beat = "R"
else:
	moves.append(input)

random.shuffle(moves)

if beat == "R":
	output = "P"
elif beat == "P":
	output = "S"
else:
	output = "R"