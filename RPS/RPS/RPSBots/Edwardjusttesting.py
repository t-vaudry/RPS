import random
output = random.choice(["R", "S", "P"])
if input == "":
	history = []
	predict = ""
history = [input] + history
for x in range(0, 5 % len(history)):
	matches = 0
	predict = history[x]
	for y in range(0, 5 % len(history)):
		if predict == history[(x + y) % len(history)]:
			matches += 1
	if matches < 1:
		predict = ""
if predict == "R":
	output = "P"
elif predict == "S":
	output = "R"
elif predict == "P":
	output = "S"