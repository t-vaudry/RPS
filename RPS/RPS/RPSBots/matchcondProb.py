import random
from collections import defaultdict

if input == "":
	fullHistory = ""
	rps = ['R', 'P', 'S']
	counterMove = {'R':'P', 'P':'S', 'S':'R'}
	counts = defaultdict(lambda: 0)
	agent = opponent = ""
	output = random.choice(rps)
else:
	fullHistory += input+output
	counts[agent+opponent+input] += 1
	for length in range(min(14, len(fullHistory)-2), 0, -2):
		string = fullHistory[-length:]
		lastFoundIndex = fullHistory.rfind(string, 0, -2)
		if lastFoundIndex != -1:
			agent = fullHistory[lastFoundIndex+length+1]
			opponent = fullHistory[lastFoundIndex+length]
			break
	movePredictions = [counts[agent+opponent+move] for move in rps]
	predictedMove = rps[movePredictions.index(max(movePredictions))]
	output = counterMove[predictedMove]