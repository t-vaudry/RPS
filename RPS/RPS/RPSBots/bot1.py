import random
if input == "":
	output = random.choice(["R","P","S"])
if input == "R" :
	output = random.choice(["P","S"])
if input == "P" : 
   output= random.choice(["R","S"])
if input == "S" : 
   output=random.choice(["S","R"])