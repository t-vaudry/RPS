import random

if input == "": #is important
	rockCount = paperCount = scissorsCount = 0
elif input == "R":
	rockCount += 1
elif input == "P":
	paperCount += 1
elif input == "S":
	scissorsCount += 1

if input == "R":
	output = random.choice(["P","S"]) 
elif input == "S":
	output = random.choice(["R","P"]) 
else:
	output = random.choice(["R","S"])