import random
from collections import defaultdict

if input == "":
	history = ""
	history2 = ""
	combine = { 'PP': '1', 
		  'PR': '2', 
		  'PS': '3',
		  'RP': '4',
		  'RS': '5',
		  'RR': '6',
		  'SS': '7',
		  'SP': '8',
		  'SR': '9',}
	split = {   '1':'PP', 
		  '2':'PR', 
		  '3':'PS',
		  '4':'RP',
		  '5':'RS',
		  '6':'RR',
		  '7':'SS',
		  '8':'SP',
		  '9':'SR',}
	rps = ['R', 'P', 'S']
	matchups = {'P': 'S', 'S': 'R', 'R': 'P'}
	stats = defaultdict(lambda: 0)
	output = random.choice(rps)
	my = opp = ""
else:
	if (random.choice([0,1]) == 0):
		if output != "":
			history += combine[output + input]

		for length in range(min(20, len(history)-1), 0, -1):
			search = history[-length:]
			index = history.rfind(search, 0, -1)
			if index != -1:
				OGanswer = history[index + length]
				guess = split[OGanswer][1]
				output = matchups[guess]
			else:
				output = random.choice(rps)
	else:
		history2 += output.lower()+input
		stats[my+opp+input] += 1
		for length in range(min(10, len(history2)-2), 0, -2):
			search = history2[-length:]
			index = history2.rfind(search, 0, -2)
			if index != -1:
				my = history2[index+length].upper()
				opp = history2[index+length+1]
				break
		predictions = [stats[my+opp+h] for h in rps]
		prediction = rps[predictions.index(max(predictions))]
		output = matchups[prediction]