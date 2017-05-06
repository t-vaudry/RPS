import random;

if input == "": # initialize variables for the first round
	rockCount = paperCount = scissorsCount = 0;
elif input == "R":
	rockCount += 1;
elif input == "P":
	paperCount += 1;
elif input == "S":
	scissorsCount += 1;

if rockCount == 0 and scissorsCount == 0 and paperCount == 0:
	output = random.choice(["R","P","S"])  # go random the first time
elif rockCount == 0 and scissorsCount == 0:
	output = "S";
elif rockCount == 0 and paperCount == 0:
	output = "R";
elif scissorsCount == 0 and paperCount == 0:
	output = "P";
else:
	if scissorsCount == 67:
		output = "R";
	elif rockCount % 4 == 0:
		output = random.choice(["R","S"])
	elif rockCount % 3 == 0:
		output = random.choice(["P","S"])
	elif rockCount % 2 == 0:
		output = random.choice(["S","P"])
	elif paperCount % 2 == 0:
		output = random.choice(["S","R"])
	else:
		output = random.choice(["R","P","S"])