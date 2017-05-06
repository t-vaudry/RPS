import random

if not input:
	options = ['R', 'P', 'S']
	beats_to = {'R': 'P', 'P': 'S', 'S': 'R'}
	beated_by = {'R': 'S', 'P': 'R', 'S': 'P'}
	fightResults = []
	my_played = []
	their_played = []
	rocks = 0
	papers = 0
	scissors = 0
	total = 0
	selection = random.choice(options)
else:
	their_played.append(input)
	rocks += input == 'R'
	papers += input == 'P'
	scissors += input == 'S'
	total += 1
	probabilities = { 'R': rocks / float(total), 'P': papers / float(total), 'S': scissors / float(total)}
	selection = min(probabilities, key=probabilities.get)
	selection = beated_by[selection]

my_played.append(selection)
output = selection