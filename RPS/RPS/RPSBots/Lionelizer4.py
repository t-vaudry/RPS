import random

if input == "": # initialize variables for the first round
	rockCount = paperCount = scissorsCount = 0
elif input == "R":
	rockCount += 1
elif input == "P":
	paperCount += 1
elif input == "S":
	scissorsCount += 1

if rockCount == 0 or paperCount == 0 or scissorsCount == 0:
	output = random.choice(["R","P","S"])
elif rockCount % random.choice([4,5,7]) == 0:
	rockCount += 1
	output = "R"
elif paperCount % random.choice([4,5,7]) == 0:
	paperCount += 1
	output = "P"
elif scissorsCount % random.choice([4,5,7]) == 0:
	scissorsCount += 1
	output = "S"
elif rockCount > paperCount and rockCount > scissorsCount:
	output = random.choice(["R","S","P","P"])
elif paperCount > scissorsCount:
	output = random.choice(["R","P","S","S"])
else:
	output = random.choice(["P","S","R","R"])