import random
if input == "":
	output = random.choice(["R","P","S"])
	lastinput=""
if input == "R" :
	output = random.choice(["R","P"])
if input == "P" : 
   output= random.choice(["P","S"])
if input == "S" : 
   output=random.choice(["S","R"])
if lastinput == output:
	if lastinput == "R":
		output=random.choice(["S","R"])
	elif lastinput == "S":
		output=random.choice(["R","S"])
	elif lastinput == "P":
		output=random.choice(["P","S"])
lastinput=input
if random.choice([1,2,3]) == 1:
	output=random.choice(["P","R"])
if random.choice(["R","P","S"]) == input:
	output=random.choice(["R","S"])