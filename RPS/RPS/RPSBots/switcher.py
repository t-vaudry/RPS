if input == '':
	score = {	'R': { 'R':  0, 'P': -1, 'S':  1 },
				'P': { 'R':  1, 'P':  0, 'S': -1 },
				'S': { 'R': -1, 'P':  1, 'S':  0 } }
	strat = ['R', 'P', 'S']
	state = 0
	delta = 1
	round = 0
	lastSwitch = round
	patience = 10
	memLen = 10
	hist = []
else:
	round += 1
	hist.append(score[input][prevMove])

if round > memLen:
	lastPoints = sum(hist[-memLen:])
	if lastPoints < 0 and round-lastSwitch > patience:
		delta = -delta
		lastSwitch = round

state = (state+delta)%len(strat)
output = strat[state]
prevMove = output