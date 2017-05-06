import random

max = 11

if input == "":
	history = ''
	opponent_model = {}
	
	
history += input


if len(history) > max:
	current_seq = history[len(history)-max:len(history)-1]
	if opponent_model.has_key(current_seq):
		opponent_model[current_seq][input] += 1			
	else:
		opponent_model[current_seq] = {}	
		opponent_model[current_seq]['R'] = 0
		opponent_model[current_seq]['P'] = 0
		opponent_model[current_seq]['S'] = 0
		opponent_model[current_seq][input] = 1	
else:
	current_seq = ""

def prob_vector(seq):
	if not opponent_model.has_key(seq):
		return {'R': 0.3333, 'P': 0.3333, 'S': 0.3333}
	else:
		total = opponent_model[seq]['R'] + opponent_model[seq]['P'] + opponent_model[seq]['S']
		p_vec = {}
		p_vec['R'] = opponent_model[seq]['R'] / float(total)
		p_vec['P'] = opponent_model[seq]['P'] / float(total)
		p_vec['S'] = opponent_model[seq]['S'] / float(total)
		return p_vec


def choice(prob_vector):
	if (random.random() < 0.1):
		return random.choice(["R", "P", "S"])
	c = random.random()
	r = 0.3
	if prob_vector['P'] > prob_vector['R'] and prob_vector['P'] > prob_vector['S']:
		if c > r:
			return 'S'
		else:
			return 'P'
	else:
		if prob_vector['R'] > prob_vector['S']:
			if c > r:
				return 'P'
			else:
				return 'R'
	if c > r:
		return 'R'	
	else:
		return 'S'

choice = choice(prob_vector(current_seq))

history += choice

output = choice