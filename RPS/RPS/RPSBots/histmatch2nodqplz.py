#simple meta history matcher
#uses stuff from http://www.ofb.net/~egnor/iocaine.html and 2 history matching predictors
#this one hist,hist2,and rand
#licatj @ no-spam-pls rpi.edu

import random

wins = ['RS','SP','PR']
		


numMeta = 3 #num of meta strategies for each predictor

if input=='': #first round; initialize everything
	myLastMove = 'X'
	currSet = 0
	score = 0
	allMoves = [] #history of all moves made
	myMoves = []
	hisMoves = []
	output = random.choice(['R','P','S'])
	#initialize strategies
	def hist(allMoves,type):
		lam = len(allMoves)
		if lam < 2:
			#print "random"
			return random.choice('RPS')
		maxDepth = 100
		maxLength = 10
		#search backwards
		candStart = lam-2 #starting point of the current candidate being considered
		currCand = candStart
		currStr = lam-1
		bestStart = candStart
		bestLen = 0
		#matchFound = False
		currDepth = 0
		while 1:#not matchFound: #search backwards
			if currCand < 0 or lam-currCand > maxDepth:
				break
			#print "comparing %s and %s" % (allMoves[currCand],allMoves[currStr])
			if allMoves[currCand] == allMoves[currStr]:
				#print "same!"
				currCand -= 1
				currStr -= 1
				if candStart-currCand > bestLen:
					bestLen = candStart-currCand
					bestStart = candStart
					if bestLen >= maxLength:
						#matchFound = True
						break
			else:
				#restart search
				currStr = lam-1
				candStart -= 1
				currCand = candStart
		#print "best len was " + str(bestLen)
		#print bestStart
		#print "returning " + allMoves[bestStart+1]
		#what we return depends on the format of the history provided
		if type==0:
			return allMoves[bestStart+1]
		else:
			return allMoves[bestStart+1]
	
	stored = ''
	def histAll():
		global allMoves,stored
		stored = hist(allMoves,0)
		#print "returned " + stored
		if len(stored)==1:
			stored = stored+stored
		return stored[0]
	def histAll2():
		global stored
		return stored[1]
		
	def rand():
		return random.choice('RPS')
		
	allStrats = [histAll,histAll2,rand]#[alwaysRock,alwaysPaper,alwaysScissors,histAll,histAll2,rand,histHis,histMines]
	allScores = []
	allPredictions = []
	for i in range(len(allStrats)*numMeta):
		allScores.append(0)
		allPredictions.append('X')
else:
	allMoves.append(myLastMove + input)
	myMoves.append(myLastMove)
	hisMoves.append(input)
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
		for i in xrange(len(allStrats)):
			for j in xrange(numMeta*i, numMeta*i+3):
				allScores[j] = max(0,allScores[j]-1) #decay
				if allPredictions[j] == input:
					allScores[j] += 20
			predBase = allStrats[i]() #update predictions:
			jumpUp = {'R':'S', 'P':'R', 'S':'P'}
			nmi = numMeta*i
			allPredictions[nmi] = predBase #P.0 : assume they'll follow the move exactly predicted
			allPredictions[nmi+1] = jumpUp[predBase] #P.1 - assume they predict we'll try to beat predBase
			allPredictions[nmi+2] = jumpUp[jumpUp[predBase]] #P.2 - assume they predict we'll try to beat jumpUp[predBase]
			#allPredictions[6*i+3] = #P'.0
		#select the best one so far
		i = allScores.index(max(allScores))
		output = {'R':'P', 'P':'S', 'S':'R'}[allPredictions[i]]
		
currSet += 1
myLastMove = output