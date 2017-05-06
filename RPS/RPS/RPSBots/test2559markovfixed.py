if input == "":
	import random
	order = 3
	history = ""
	output = random.choice(["R", "P", "S"])
else:
	history += input
	if len(history) >= order:
		search = history[-order:]
		mplace = history.rfind(search, 0, len(history)-3)
		predict = history[mplace+3]
		if predict == "R":
			output = "P"
		elif predict == "P":
			output = "S"
		elif predict == "S":
			output = "R"
		else:
			output = random.choice(["R","P","S"])
	else:
		output = random.choice(["R","P","S"])