import random;

if input == "": # initialize variables for the first round
	count = 0;

count += 1;

if count % 2 == 0:

	if input == "R":
		output = "S";
	elif input == "P":
		output = "R";
	elif input == "S":
		output = "P";
		
else:
	output = random.choice(["R","P","S"]);