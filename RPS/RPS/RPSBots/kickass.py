import random
if input == "": # initialize variables for the first round
	rockCount = paperCount = scissorsCount = stratecount = 0
elif input == "R":
	rockCount += 1
	stratecount += 1
elif input == "P":
	paperCount += 1
	stratecount += 1
elif input == "S":
	scissorsCount += 1
	stratecount += 1
if stratecount > 3:
	output = random.choice(["R","P","S"])
	stratecount = 0
if rockCount > paperCount and rockCount > scissorsCount:
	output = "P" # paper beats rock
elif paperCount > scissorsCount:
	output = "S" # scissors beats paper
else:
	output = "R" # rock beats scissors