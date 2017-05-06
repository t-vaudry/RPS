import random;

if input == "": # initialize variables for the first round
	count = 0;


if count % 2 == 0:

	if input == "R":
		output = "S";
	elif input == "P":
		output = "R";
	elif input == "S":
		output = "P";
	else:
		output = random.choice(["R","P","S"]);

else:
	count += 1;
	output = random.choice(["R","P","S"]);