import random
if input == "": # initialize variables for the first round
        output = random.choice(["R","P","S"])
        last = random.choice(["R","P","S"])
elif input == "R" and last == "R":
	output = "S"
elif input == "P" and last == "P":
	output = "R"
elif input == "S" and last == "S":
	output = "P"
else:
        output = random.choice(["R","P","S"])

last=input