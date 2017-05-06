import random
output = random.choice(["R", "S", "P"])
if input == "":
	history = []
	guess = ""
	x = 0
else:
	history = [input] + history
	x = 0
	while ((x + 1 < len(history) and (history[min(x, len(history) - 1)] != history[min(x + 1, len(history) - 1)]))):
		x += 1
	guess = history[min(x, len(history) - 1)]
if guess == "R":
	output = "P"
elif guess == "S":
	output = "R"
elif guess == "P":
	output = "S"