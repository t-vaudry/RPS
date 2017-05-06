import math
import random

def predict(history, decay, last):
	scores = [0.0, 0.0, 0.0]
	
	def score(age, length):
		return length / math.log(age + 1.0)
		#return (decay ** age) * (1.0 - decay ** length) / (1.0 - decay)
	def add_score(start, end):
		scores[history[start + 1]] += score(last - start, start - end)
		
	matches = []
	for i in range(last - 1, max(-1, last - 33), -1):
		j = 0
		while j < len(matches):
			match = matches[j]
			match[0] -= 1
			if history[i] != history[match[0]]:
				add_score(match[1], i)
				matches.pop(j)
			j += 1
		if history[i] == history[last]:
			matches.append([last, i])
	for match in matches:
		add_score(match[1], -1)
	return scores

if not input:
	time = 0
	
	hands = {
		'R': 0,
		'P': 1,
		'S': 2
	}
	
	my_history = []
	opp_history = []
	
	output = 'RPS'[random.randint(0, 2)]
else:
	my_history.append(hands[output])
	opp_history.append(hands[input])
	
	my_pred = predict(my_history, 0.98, len(my_history) - 1)
	opp_pred = predict(opp_history, 0.98, len(opp_history) - 1)
	
	rand_factor = 0.1
	
	pred = [
		my_pred[1] - my_pred[0] + opp_pred[2] - opp_pred[1] + random.random() * rand_factor,
		my_pred[2] - my_pred[1] + opp_pred[0] - opp_pred[2] + random.random() * rand_factor,
		my_pred[0] - my_pred[2] + opp_pred[1] - opp_pred[0] + random.random() * rand_factor
	]
	
	m = max(pred)
	if m == pred[0]:
		output = 'R'
	elif m == pred[1]:
		output = 'P'
	elif m == pred[2]:
		output = 'S'
	else:
		output = ''
	
	time += 1