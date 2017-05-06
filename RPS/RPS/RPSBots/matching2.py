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
	matchIndices = []
	flag = 0
	for i in range(0, len(tempHistory), 2):
		string = tempHistory[i:]
		lastFoundIndex = fullHistory.rfind(string, 0, len(fullHistory))
		index = lastFoundIndex + len(string)
		if lastFoundIndex != -1 and len(fullHistory) > index:
			flag = 1
			predictedInput = fullHistory[index]
			output = counterMove[predictedInput]
			break
	if flag == 0:
		output = random.choice(rps)