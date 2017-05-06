import random
output = random.choice(["R", "P", "S"]) # usually gets reassigned
if input == "": # initialize variables for the first round
	rockCount = paperCount = scissorsCount = 0
elif input == "R":
	rockCount += 1
elif input == "P":
	paperCount += 1
elif input == "S":
	scissorsCount += 1
if rockCount < paperCount and rockCount < scissorsCount: # pick what beats the rarest
	output = "P" # paper beats rock
elif paperCount < rockCount and paperCount < scissorsCount:
	output = "S" # scissors beats paper
elif scissorsCount < paperCount and scissorsCount < rockCount:
	output = "R" # rock beats scissors