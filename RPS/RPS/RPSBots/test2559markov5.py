if input == "":
	import random
	order = 5
	history = ""
	output = random.choice(["R", "P", "S"])
else:
	history += input
	if len(history) >= order:
		search = history[-order:]
		mplace = history.rfind(search, 0, len(history)-order)
		predict = history[mplace+order]
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