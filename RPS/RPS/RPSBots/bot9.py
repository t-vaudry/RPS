import random
if input == "":
	output = random.choice(["R","P","S"])
	lastinput=""
	input = output
if input == "R" :
	output = random.choice(["R","P"])
if input == "P" : 
   output= random.choice(["P","S"])
if input == "S" : 
   output=random.choice(["S","R"])
lastinput=input
if random.choice([1,2,3]) == 2:
	output=random.choice(["P","R","S"])
if random.choice(["R","P","S"]) == input:
	output=random.choice(["R","S"])
if random.choice([1,2,3,4,5]) == 3:
	output=random.choice(["S","P","R"])
if random.choice([1,2,3,4,5,6,7]) == 4:
	output="S"
if random.choice([1,2,3,4,5,6,7,8,9]) == 5:
	output="P"
if random.choice([1,2,3,4,5,6,7,8,9,10,11]) == 6:
	output="R"