import random

if input == "": # initialize variables for the first round
	rockCount = paperCount = scissorsCount = winCount = loseCount = offset = lastResult = enemyResult = 0
	rock = 0
	paper = 1
	scissors = 2
	result = random.choice([0,1,2])
elif input == "R":
	enemyResult = 0
	rockCount += 1
elif input == "P":
	enemyResult = 1
	paperCount += 1
elif input == "S":
	enemyResult = 2
	scissorsCount += 1

victory = (lastResult-enemyResult)%3

if victory == 1:
	winCount += 1
elif victory == 2:
	loseCount += 1

if (winCount+loseCount) > 10 and loseCount > winCount:
	offset = (offset-1)%3

if rockCount > paperCount and rockCount > scissorsCount:
	result = 1 # paper beats rock
elif paperCount > scissorsCount and paperCount > rockCount:
	result = 2 # scissors beats paper
elif scissorsCount > rockCount and scissorsCount > paperCount:
	result = 0 # rock beats scissors
else:
	result = random.choice([0,1,2])

result = (result+offset)%3

if result == 0:
	output = "R"
elif result == 1:
	output = "P"
else:
	output = "S"