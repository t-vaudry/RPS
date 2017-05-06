#simple history matcher

import random

wins = ['RS','SP','PR']
		


numMeta = 3 #num of meta strategies for each predictor

if input=='': #first round; initialize everything
	myLastMove = 'X'
	currSet = 0
	score = 0
	allMoves = [] #history of all moves made
	output = random.choice(['R','P','S'])
	#initialize strategies
	def hist():
		global allMoves
		maxDepth = 200
		maxLength = 20
		numChanged = 2
		currI = len(allMoves)-2
		candidates = []
		candCurrs = []
		lengths = []
		disabled = []
		currDepth = 0
		numChecked = 0
		maxToCheck = 5
		for i in range(len(allMoves)-1):
			if allMoves[i]==allMoves[-1]:
				candidates.append(i)
				candCurrs.append(i-1)
				lengths.append(1)
				disabled.append(False)
				numChecked += 1
			if numChecked >= maxToCheck:
				break
		#print "cand:"
		#print candCurrs
		ml=0
		while numChanged > 1 and currDepth < maxDepth and ml < maxLength:
			currDepth += 1
			numChanged = 0
			for i in range(len(candCurrs)):
				if candCurrs[i] < 0 or disabled[i]:
					continue
				if allMoves[currI]==allMoves[candCurrs[i]]:
					numChanged += 1
					lengths[i] += 1
					candCurrs[i] -= 1
				else:
					disabled[i] = True
			currI -= 1
			
		if len(lengths) > 0:
			#print "Found sequence of length " + str(max(lengths))
			ml = max(lengths)
			pred = allMoves[candidates[lengths.index(ml)]+1][1]
			#print "Prediction is " + pred
			return pred
		else:
			return random.choice(['R','P','S'])
		
	allStrats = [hist] #all should return [a,b] where a is in [0,1] and b is 'R','P',or 'S'
	allScores = []
	allPredictions = []
	for i in range(len(allStrats)*numMeta):
		allScores.append(0)
		allPredictions.append('X')
else:
	allMoves.append(myLastMove + input)
	scoreChange = 0
	if (myLastMove+input) in wins:
		score += 1
		scoreChange = 1
	elif (input+myLastMove) in wins:
		score -= 1
		scoreChange = -1
		
	if currSet >= 500 and score < 0:
		output = random.choice(['R','P','S']) #resort to random strategy
	else: #actually try something
		output = 'R'
		for i in range(len(allStrats)):
			for j in range(i, i+numMeta):
				if allPredictions[j] == input:
					allScores[j] += 1
			predBase = allStrats[i]() #update predictions:
			jumpUp = {'R':'S', 'P':'R', 'S':'P'}
			allPredictions[numMeta*i] = predBase #P.0 : assume they'll follow the move exactly predicted
			allPredictions[numMeta*i+1] = jumpUp[predBase] #P.1 - assume they predict we'll try to beat predBase
			allPredictions[numMeta*i+2] = jumpUp[jumpUp[predBase]] #P.2 - assume they predict we'll try to beat jumpUp[predBase]
			#allPredictions[6*i+3] = #P'.0
		#select the best one so far
		i = allScores.index(max(allScores))
		output = allPredictions[i]
	#print allMoves
	#print allScores
	#print "next you'll choose " + output
	#output = 'R'
		
currSet += 1
myLastMove = output