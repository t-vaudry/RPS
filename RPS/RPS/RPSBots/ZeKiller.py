import random

if input == "": # initialize variables for the first round
	rockCount = paperCount = scissorsCount = 0
elif input == "R":
	rockCount += 1
elif input == "P":
	paperCount += 1
elif input == "S":
	scissorsCount += 1
if rockCount*0.75 > paperCount and rockCount*0.75 > scissorsCount:
	output = "P" # paper beats rock
elif paperCount*0.75 > scissorsCount and paperCount*0.75 > rockCount:
	output = "S" # scissors beats paper
elif scissorsCount*0.75 > rockCount and scissorsCount *0.75 > paperCount:
	output = "R" # rock beats scissors
else:
	output = random.choice(["R","P","S"])