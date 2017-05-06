import random

r = random.randrange(0,2)
if r==0 or r==1:
	move = random.randrange(0,3)
	if move == 1:
		output = "R"
	elif move == 2:
		output = "P"
	else:
		output = "S"
elif r==2:
	if input=="": # initialize variables for the first round
		rockCount = paperCount = scissorsCount = 0
	if input == "R":
		rockCount += 1
	elif input == "P":
		paperCount += 1
	elif input == "S":
		scissorsCount += 1
	if rockCount > paperCount and rockCount > scissorsCount:
		output = "P" # paper beats rock
	elif paperCount > scissorsCount:
		output = "S" # scissors beats paper
	else:
		output = "R" # rock beats scissors