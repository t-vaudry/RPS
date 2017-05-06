# This bot looks at the opponent's two previous moves and chooses a move that
# doesn't lose against either one.
# 2013-10-02

import random

previnput = ""

# Make random move for the first round
if input == "":
	output = random.choice (["R", "P", "S"])
else:
	if previnput == "":
		output = input
	else:
		if previnput == input:
			if input == "R":
				output = random.choice (["R", "P"])
			elif input == "S":
				output = random.choice (["S", "R"])
			else:
				output = random.choice (["P", "S"])
		else:
			if (input == "R" and previnput == "P") or (input == "P" and previnput == "R"):
				output = "P"
			elif (input == "P" and previnput == "S") or (input == "S" and previnput == "R"):
				output = "S"
			else:
				output = "R"

previnput = input