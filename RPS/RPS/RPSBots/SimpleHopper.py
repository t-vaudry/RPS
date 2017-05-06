import random

count = random.randrange(1, 10)
choice = random.choice(["R","P","S"])

if(count == 0):
	count = random.randrange(1, 10)
	choice = random.choice(["R","P","S"])

count -= 1

output = choice;