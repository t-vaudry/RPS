import random

while True:
	x = ["R","P","S"]
	r = random.randint(0,2)
	random.shuffle(x)
	output = x[r]
	break