import random

if input == "": # initialize variables for the first round
	count = 0
elif input != "":
        count += 1

if count < 700:
        output = random.choice(["R","P"])
elif count > 699:
        output = "S"