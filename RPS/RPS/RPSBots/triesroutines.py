import random

recordOutput = False

rate = 25
decay = 1
allRoutines = ['RRR', 'RRP', 'RRS', 'RPR', 'RPP', 'RPS', 'RSR', 'RSP', 'RSS',
'PRR', 'PRP', 'PRS', 'PPR', 'PPP', 'PPS', 'PSR', 'PSP', 'PSS',
'SRR', 'SRP', 'SRS', 'SPR', 'SPP', 'SPS', 'SSR', 'SSP', 'SSS']
wins = ['RS','SP','PR']

if input=='': #first round; initialize everything
	scores = [100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]
	currRoutine = 23
	currStep = 0
	currWins = 0
	myLastMove = 'X'
#else:


if currStep < 3:
	output = allRoutines[currRoutine][currStep]
	currStep += 1
	if myLastMove + output in wins:
		currWins += rate
	elif output + myLastMove in wins:
		currWins -= rate
else:
	#update scores
	scores[currStep] += currWins
	if scores[currStep] < 0:
		scores[currStep] = 0
	#decay
	for i in range(len(scores)):
		if scores[i]<100:
			scores[i]+=decay
		elif scores[i]>100:
			scores[i]-=decay
	#choose new routine
	weights = []
	total = 0.0
	for s in scores:
		total += s*1.0
	for s in scores:
		weights.append(1.0*s/total)
	r = random.random()
	currRoutine = len(allRoutines)-1
	t = 0.0
	for i in range(len(allRoutines)):
		 t += weights[i]
		 if r <= t:
		 	currRoutine = i
		 	break	
	
	#reset
	currStep = 1
	currWins = 0
	output = allRoutines[currRoutine][0]
	#print currRoutine
	
	
myLastMove = output