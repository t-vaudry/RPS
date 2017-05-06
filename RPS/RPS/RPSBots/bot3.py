import random
if input == "":
	output = random.choice(["R","P","S"])
	lastinput=""
if input == "R" :
	output = random.choice(["P","S"])
if input == "P" : 
   output= random.choice(["S","P"])
if input == "S" : 
   output=random.choice(["S","R"])
if lastinput == output:
	if lastinput == "R":
		output=random.choice(["S","P"])
	elif lastinput == "S":
		output=random.choice(["R","S"])
	elif lastinput == "P":
		output=random.choice(["P","R"])
lastinput=input
if random.choice([1,2,3]) == 1:
	output=random.choice(["S","R"])