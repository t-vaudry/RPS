import random 

if input == "":
	score = 0
	lastMove = "X"
	inputCount = { 'R': 0, 'P': 0, 'S': 0 }
else:
	inputCount[input] += 1

if lastMove != input:
	if lastMove == "R" and input == "P":
		score -= 1
	elif lastMove == "R" and input == "S":
		score += 1
	elif lastMove == "P" and input == "R":
		score += 1
	elif lastMove == "P" and input == "S":
		score -= 1
	elif lastMove == "S" and input == "R":
		score -= 1
	elif lastMove == "S" and input == "P":
		score += 1

if score > 0:
	c, m = max(inputCount.iteritems())
	lastMove = "R"
	output = "R"
else:
	lastMove = random.choice(["R", "P", "S"]) 
	output = lastMove