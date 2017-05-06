if input == "":
	last = "R"
	output = "R"
if last == "R":
	last = "P"
	output = "P"
elif last == "P":
	last = "S"
	output = "S"
elif last == "S":
	last = "R"
	output = "R"