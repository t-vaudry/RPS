import math
import random

r = random.randrange(0,2)
if r==0 or r==1:
	move = random.randrange(0,3)
	if move == 1:
		output = "R"
	elif move == 2:
		output = "P"
	else:
		output = "S"
elif r==2:
	if not input:
	    	output = 'P'
	else:
	    	output = {'R':'P', 'P':'S', 'S':'R'}[input]