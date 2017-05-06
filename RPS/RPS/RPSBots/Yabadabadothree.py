import random

if input == "":
	round = 0

if round < 333:
        output = random.choice(["R","P"])
elif round < 666:
        output = random.choice(["R","S"])
else:
        output = random.choice(["P","S"])

round += 1