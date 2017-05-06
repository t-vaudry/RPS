import random
from collections import defaultdict

if (random.choice([0,1]) == 0):
	if input == "":
		history = ""
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
		history1 = ""
		rps = ['R', 'P', 'S']
		matchups = {'P': 'S', 'S': 'R', 'R': 'P'}
		stats = defaultdict(lambda: 0)
		output = random.choice(rps)
		my1 = opp1 = ""
	else:
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
				output = random.choice(['R', 'P', 'S'])
else:
	if input == "":
		history = ""
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
		history1 = ""
		rps = ['R', 'P', 'S']
		matchups = {'P': 'S', 'S': 'R', 'R': 'P'}
		stats = defaultdict(lambda: 0)
		output = random.choice(rps)
		my1 = opp1 = ""
	else:
		history1 += output.lower()+input
		stats[my1+opp1+input] += 1
		for length in range(min(10, len(history)-2), 0, -2):
			search1 = history1[-length:]
			index1 = history1.rfind(search1, 0, -2)
			if index1 != -1:
				my1 = history1[index1+length].upper()
				opp1 = history1[index1+length+1]
				break
		predictions1 = [stats[my1+opp1+h] for h in rps]
		prediction1 = rps[predictions1.index(max(predictions1))]
		output = matchups[prediction1]