import random

BEAT  =  {'R': 'P', 'P': 'S', 'S': 'R', '': ''}
N_SOLUTIONS = 12
MAX_SEARCH = 12

def score(input, output):
	if input == output: return 0
	if BEAT[input] == output: return 1
	return -1 

if input  ==  '': # Initialize variables for the first round
	rival_history = ''
	self_history = ''
	output = random.choice('RPS')
	self_history = output
	solutions = [''] * N_SOLUTIONS
	scores = [0.0] * N_SOLUTIONS
else:
	for i in range(N_SOLUTIONS):
		if solutions[i] != '':
			scores[i] *= 0.9
			bonus = score(input, solutions[i])
				
			scores[i] += bonus
	rival_history = input + rival_history

	# Solution 0 - Predict Rival, attempt to win
	solutions[0] = ''
	length = MAX_SEARCH
	index = -1
	
	expected_rival = ''
	while index == -1 and length > 0:
		index = rival_history.find(rival_history[0:length-1], 1)
		length -= 1
		
	if length != 0:
		expected_rival = rival_history[index-1]
		
	solutions[0] = BEAT[expected_rival]

	# Solution 1 - Predict self, attempt to win
	solutions[1] = ''
	length = MAX_SEARCH
	index = -1
	
	expetcted_self = ''
	while index == -1 and length > 0:
		index = self_history.find(self_history[0:length-1],1)
		length -= 1

	if length != 0:
		expetcted_self = self_history[index-1]

	solutions[1] = BEAT[BEAT[expetcted_self]]

	# Solution 2 - Random
	solutions[2] = random.choice('RPS')

	# Solution 3 - Predict Rival, force tie
	solutions[3] = expected_rival

	# Solution 4 - Predict Rival, attempt to lose
	solutions[4] = BEAT[BEAT[expected_rival]]

	# Solution 5 - Predict self, play predictable
	solutions[5] = expetcted_self

	# Solution 6 - Predict self, force tie
	solutions[6] = BEAT[expetcted_self]

	# Solution 7 - Repeat Self
	solutions[7] = output

	# Solution 8 - Repeat Rival
	solutions[8] = input

	# Solution 9 - Rival assumes repeating
	solutions[9] = BEAT[output]
	
	# Solution 10 - Predict self, choose randomly one of the two unexpected options
	solutions[10] = random.choice('RPS'.replace(expetcted_self, ''))
	
	# Solution 11 - Predict rival, assumes it chooses randomly one of the two unexpected options
	solutions[11] = BEAT[random.choice('RPS'.replace(expetcted_self, ''))]
	
	best = -1
	for i in range(N_SOLUTIONS):
		if scores[i] > best and solutions[i] != '':
			best = scores[i]
			output = solutions[i]
			best_i = i
		elif -scores[i] > best and solutions[i] != '':
			# This solution is actually REALLY good at losing!
			best = -scores[i]
			output = BEAT[BEAT[solutions[i]]]
			best_i = i
	
	scores[best_i] *= 0.8
			
	self_history = output + self_history