#simple meta matcher
#uses stuff from http://www.ofb.net/~egnor/iocaine.html , 2 history matchers and 2 frequency predictors
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
			#aprint "random"
			return 'X'#random.choice('RPS')
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
			#cprinte "comparing %s and %s" % (allMoves[currCand],allMoves[currStr])
			if allMoves[currCand] == allMoves[currStr]:
				#bprint "same!"
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
		#dprintg "best len was " + str(bestLen)
		#eprintf bestStart
		#fprintq "returning " + allMoves[bestStart+1]
		#what we return depends on the format of the history provided
		if type==0:
			return allMoves[bestStart+1]
		else:
			return allMoves[bestStart+1]

	stored = ''
	def histAll():
		global allMoves,stored
		stored = hist(allMoves,0)
		#gprintw "returned " + stored
		if len(stored)==1:
			stored = stored+stored
		return stored[0]
	def histAll2():
		global stored
		return stored[1]
	
	def histHis(): #only uses opponent's history
		global hisMoves
		return hist(hisMoves,1)
	
	def histMines(): 
		global myMoves
		return hist(myMoves,1)

	def rand():
		return random.choice('RPS')
		
	frq = [0,0,0]
	def freq(): #only looks at what moves they made and what probability it is, tries to tie or beat it
		global allMoves,frq
		#learn from last move made
		if len(allMoves)==0:
			return 'X'
		frq[ 'RPS'.index(allMoves[-1][1]) ] += 1
		a = [frq[0]+frq[1], frq[1]+frq[2], frq[2]+frq[0]]
		return 'PSR'[ a.index(max(a)) ] #return move most likely to draw or win
			
	frq2 = [0,0,0]
	def freq2(): #like freq, but assumes they think we're playing with freq and they want to beat it
		global allMoves,frq2
		#learn from last move made
		if len(allMoves)==0:
			return 'X'
		frq2[ 'RPS'.index(allMoves[-1][0]) ] += 1
		a = [frq[0]+frq[1], frq[1]+frq[2], frq[2]+frq[0]]
		r = 'PSR'[ a.index(max(a)) ]
		return {'R':'P', 'P':'S', 'S':'P'}[r]
		
	
	allStrats = [freq,freq2,histAll,histAll2,rand]#,markov1,markov2,alwaysRock,alwaysPaper,alwaysScissors,,histHis,histMines]
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
					allScores[j] += 5
			predBase = allStrats[i]() #update predictions:
			jumpUp = {'R':'S', 'P':'R', 'S':'P', 'X':'S'}
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