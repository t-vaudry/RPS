import random
winners = {'P': 'S', 'R': 'P', 'S': 'R'}
if input == '':
	i = 0
	output = random.choice(['R', 'P', 'S'])
else:
	output = winners[input]