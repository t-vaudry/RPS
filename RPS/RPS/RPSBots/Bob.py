import random
output = random.choice(["R", "S", "P"])
if input == "":
	a = ""
	b = ""
else:
	a = b
	b = input
if a == b:
	if b == "R":
		output = "S"
	elif b == "S":
		output = "P"
	elif b == "P":
		output = "R"
	elif b == "":
		output = random.choice(["R", "S", "P"])
else:
	if a == "R":
		if b == "S":
			output = "S"
		elif b == "P":
			output = "R"
	elif a == "S":
		if b == "R":
			output = "S"
		elif b == "P":
			output = "P"
	elif a == "P":
		if b == "S":
			output = "P"
		elif b == "R":
			output = "R"