import random
if input == "":
	output = random.choice(["R","P","S"])
	lastinput=""
if lastinput == "R" :
	output = random.choice(["R","P"])
if lastinput == "P" : 
   output= random.choice(["P","S"])
if lastinput == "S" : 
   output=random.choice(["S","R"])
lastinput=input
if random.choice([1,2,3]) == 2:
	output=random.choice(["P","R","S"])
if random.choice(["R","P","S"]) == input:
	output=random.choice(["R","S"])