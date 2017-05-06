import random
output = random.choice(["R", "S", "P"])
if input == "":
	history = []
	guess = ""
else:
	history = [input] + history
	for x in [9, 8, 7, 6, 5, 4, 3]:
		if history[min(x, len(history) - 1)] == history[min(x + 1, len(history) - 1)]:
			guess = history[min(x, len(history) - 1)]
if guess == "R":
	output = "P"
elif guess == "S":
	output = "R"
elif guess == "P":
	output = "S"