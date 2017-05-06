import random

if input == "": # initialize variables for the first round
        output = random.choice(["R","P","S"])
elif input == "R":
	if output == "R":
                output = random.choice(["R","P","P","P","S","S"])
        elif output == "P":
				output = random.choice(["R","R","R","P","S","S"])
        else:
				output = random.choice(["R","R","R","P","S","S"])
elif input == "P":
	if output == "R":
				output = random.choice(["R","R","R","P","S","S"])
        elif output == "P":
				output = random.choice(["R","R","R","P","S","S"])
        else:
				output = random.choice(["R","R","R","P","S","S"])
else:
	if output == "R":
                output = random.choice(["R","P","P","P","S","S"])
        elif output == "P":
				output = random.choice(["R","R","R","P","S","S"])
        else:
				output = random.choice(["R","R","R","P","S","S"])