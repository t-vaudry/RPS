import random
output = random.choice(["R", "S", "P"])
if input == "":
	history = []
	guess = ""
else:
	history = [input] + history
	guess = history[random.choice([3, 6]) % len(history)]
if guess == "R":
	output = "P"
elif guess == "S":
	output = "R"
elif guess == "P":
	output = "S"