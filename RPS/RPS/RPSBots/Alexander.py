import random
output = random.choice(["R", "S", "P"])
if input == "R":
	output = "S"
elif input == "S":
	output = "P"
elif input == "P":
	output = "R"