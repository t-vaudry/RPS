import random



if input == "": # initialize variables for the first round
	rockCount = paperCount = scissorsCount = 0
elif output == "R":
	rockCount += 1
elif output == "P":
	paperCount += 1
elif output == "S":
	scissorsCount += 1


if input == "": # initialize variables for the first round
	rockCount1 = paperCount1 = scissorsCount1 = 0
elif input == "R":
	rockCount1 += 1
elif input == "P":
	paperCount1 += 1
elif input == "S":
	scissorsCount1 += 1

output = random.choice(["R","P","S"])

if scissorsCount1 - rockCount > 0:
	output = "S"
if rockCount1 - paperCount > 0:
	output = "R"
if paperCount1 - scissorsCount > 0:
	output = "P"

if random.random() < 0.25 :
	output = random.choice(["R","P","S"])