import random
output = random.choice(["R", "S", "P"])
if input == "R":
	output = random.choice("RSS")
elif input == "S":
	output = random.choice("SPP")
elif input == "P":
	output = random.choice("PRR")