import random

if input == "": # initialize variables for the first round
        output = random.choice(["R","P","S"])
elif input == "R":
	if output == "R":
				output = random.choice(["R","R","R","P","S","S"])
        elif output == "P":
				output = random.choice(["R","R","P","P","P","S"])
        else:
                output = random.choice(["R","R","P","P","P","S"])
elif input == "P":
	if output == "R":
				output = random.choice(["R","R","P","P","P","S"])
        elif output == "P":
				output = random.choice(["R","R","P","P","P","S"])
        else:
                output = random.choice(["R","P","P","P","S","S"])
else:
	if output == "R":
				output = random.choice(["R","R","R","P","S","S"])
        elif output == "P":
				output = random.choice(["R","R","P","P","P","S"])
        else:
                output = random.choice(["R","P","P","P","S","S"])