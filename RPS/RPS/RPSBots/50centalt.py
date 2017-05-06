if input == "": # initialize variables for the first round
	rockCount = paperCount = scissorsCount = loseCount = winCount = tieCount = 0
elif input == "R":
	tieCount = (tieCount + 1) if (last == "R") else tieCount
	winCount = (winCount + 1) if (last == "P") else winCount
	loseCount = (loseCount + 1) if (last == "S") else loseCount
	rockCount += 1
elif input == "P":
	tieCount = (tieCount + 1) if (last == "P") else tieCount
	winCount = (winCount + 1) if (last == "S") else winCount
	loseCount = (loseCount + 1) if (last == "R") else loseCount
	paperCount += 1
elif input == "S":
	tieCount = (tieCount + 1) if (last == "S") else tieCount
	winCount = (winCount + 1) if (last == "R") else winCount
	loseCount = (loseCount + 1) if (last == "P") else loseCount
	scissorsCount += 1

if rockCount > paperCount and rockCount > scissorsCount:
	output = "P" # paper beats rock
elif paperCount > scissorsCount:
	output = "S" # scissors beats paper
else:
	output = "R" # rock beats scissors
	
if tieCount > loseCount and tieCount > winCount:
	if output == "R":
		output = "P"
	elif output == "P":
		output = "S"
	else:
		output = "R"
elif loseCount > winCount:
	if output == "R":
		output = "S"
	elif output == "P":
		output = "R"
	else:
		output = "P"

if output == "R":
	output = "S"
elif output == "P":
	output = "R"
else:
	output = "P"
	
last=output