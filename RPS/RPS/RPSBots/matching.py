import random

rps = ['R', 'P', 'S']
tempHistoryLength = 10


if not input:
	fullHistory = ""
	tempHistory = ""
	counterMove = {'R':'P', 'P':'S', 'S':'R'}
	output = random.choice(rps)
else:
	if output:
		gameRound = input+output
		fullHistory += gameRound
		if len(tempHistory) == tempHistoryLength:
			tempHistory = tempHistory[2:] + gameRound
		else:
			tempHistory += gameRound
	lastFoundIndex = fullHistory.rfind(tempHistory, 0, len(fullHistory))
	if lastFoundIndex == -1:
		output = random.choice(rps)
	else:
		index = lastFoundIndex + len(tempHistory)
		if len(fullHistory) == index:
			output = random.choice(rps)
		else:
			predictedInput = fullHistory[index]
			output = counterMove[predictedInput]