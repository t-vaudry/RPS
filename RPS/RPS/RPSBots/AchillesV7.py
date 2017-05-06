import random

if input == "": # initialize variables for the first round
	rockCount = paperCount = scissorsCount = winCount = loseCount = drawCount = offset = lastResult = enemyResult = 0
	rock = 0
	paper = 1
	scissors = 2
	result = random.choice([0,1,2])
	limit = random.choice([40,30,35])
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
else:
	drawCount += 1

if (winCount+loseCount+drawCount) > limit and loseCount > winCount:
	offset = (offset-1)%3
	loseCount = winCount = drawCount = 0
	limit = random.choice([40,30,35])

if rockCount > 2*paperCount and rockCount > 2*scissorsCount:
	result = 1 # paper beats rock
elif paperCount > 2*scissorsCount and paperCount > 2*rockCount:
	result = 2 # scissors beats paper
elif scissorsCount > 2*rockCount and scissorsCount > 2*paperCount:
	result = 0 # rock beats scissors
else:
	result = random.choice([0,1,2])

result = (result+offset)%3

lastResult = result

if result == 0:
	output = "R"
elif result == 1:
	output = "P"
else:
	output = "S"