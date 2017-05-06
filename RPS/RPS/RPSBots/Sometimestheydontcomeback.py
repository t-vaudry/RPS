import random;

# assume they won't usually roll the same item twice in a row
if input == "R": 
	output = random.choice(["R","S"]);
elif input == "P": 
	output = random.choice(["R","P"]);
elif input == "S": 
	output = random.choice(["P","S"]);
else:
	# first throw
	output = random.choice(["R","P","S"]);