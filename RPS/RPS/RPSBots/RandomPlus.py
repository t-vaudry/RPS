#this program's purpose is to use frequency analysis to improve upon a simple random choice generator
#best case scenario, an algorithm will favor one choice and the program will likely defeat it
#worst(and likely) case scenario, this program will have 50% chance of winning

import random

if input == "":
	x = 34
	y = 67
elif input == "P":
	if x > 2:
		x = x - 1
		y = y - 1
elif input == "R":
	if y > x + 1:
		y = y + 1
elif input == "S":
	if x < y - 1:
		x = x + 1

n = random.randint(1,100)

if n < x:
	output = "R"
elif n < y:
	output = "P"
else:
	output = "S"