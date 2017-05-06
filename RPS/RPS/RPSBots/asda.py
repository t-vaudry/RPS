import random
from collections import defaultdict
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
	matchups = {'P': 'S', 'R': 'P', 'S': 'R'}
	rps = ['R', 'P', 'S']
	matchups = {'P': 'S', 'S': 'R', 'R': 'P'}
	stats = defaultdict(lambda: 0)
	output = random.choice(rps)
	my = opp = ""
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