import random

if not input:
	options = ['R', 'P', 'S']
	beats_to = {'R': 'P', 'P': 'S', 'S': 'R'}
	beated_by = {'R': 'S', 'P': 'R', 'S': 'P'}
	points = {'RR': 0, 'RP': -1, 'RS': 1, 'PR': 1, 'PP': 0, 'PS': -1, 'SR': -1, 'SP': 1, 'SS': 0}
	my_played = []
	their_played = []
	ocurrences = {'R': 0,	'P': 0,	'S': 0}
	total = 0
	random_play = True
else:
	their_played.append(input)
	ocurrences['R'] += input == 'R'
	ocurrences['P'] += input == 'P'
	ocurrences['S'] += input == 'S'
	total += 1
	probabilities = { 'R': ocurrences['R'] / float(total), 'P': ocurrences['P'] / float(total), 'S': ocurrences['S'] / float(total)}
	if ocurrences[max(ocurrences, key=ocurrences.get)] >= (ocurrences[min(ocurrences, key=ocurrences.get)] + 100):
		selection = max(probabilities, key=probabilities.get)
		selection = beats_to[selection]
	else:
		selection = max(probabilities, key=probabilities.get)
		selection = beated_by[selection]

if random_play:
	selection = random.choice(options)

my_played.append(selection)
output = selection
random_play = False