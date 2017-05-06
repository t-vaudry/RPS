# Inspired from the submission 'rfinds'

import random
from collections import defaultdict

if input == "":
	fullHistory1 = ""
	fullHistory2 = ""
	rps = ['R', 'P', 'S']
	counterMove = {'R':'P', 'P':'S', 'S':'R'}
	counts = defaultdict(lambda: 0)
	agent = opponent = ""
	output = random.choice(rps)
else:
	if (random.choice([0,1]) == 0):
		if output != "":
			fullHistory1 += input + output

		for length in range(min(30, len(fullHistory1)-2), 0, -2):
			string = fullHistory1[-length:]
			index = fullHistory1.rfind(string, 0, -2)
			if index != -1:
				predictedMove = fullHistory1[index + length]
				output = counterMove[predictedMove]
			else:
				output = random.choice(rps)
	else:
		fullHistory2 += input+output
		counts[agent+opponent+input] += 1
		for length in range(min(14, len(fullHistory2)-2), 0, -2):
			string = fullHistory2[-length:]
			lastFoundIndex = fullHistory2.rfind(string, 0, -2)
			if lastFoundIndex != -1:
				agent = fullHistory2[lastFoundIndex+length+1]
				opponent = fullHistory2[lastFoundIndex+length]
				break
		movePredictions = [counts[agent+opponent+move] for move in rps]
		predictedMove = rps[movePredictions.index(max(movePredictions))]
		output = counterMove[predictedMove]