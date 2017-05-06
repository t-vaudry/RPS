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
	c = random.random()
	if c < prob_vector['R']:
		return 'R'
	if c < prob_vector['R'] + prob_vector['P']:
		return 'P'
	return 'S'	

choice = choice(prob_vector(current_seq))

history += choice

output = choice