#uses stuff from http://www.ofb.net/~egnor/iocaine.html , 2 types of history matchers and 2 frequency predictors
#hist() matcher code and final metastrat. selector influenced by momo's 'galton' bot
#also has a metameta level for those predictors that somehow figure me out
#licatj @ no-spam-pls rpi.edu

import random
from collections import defaultdict

wins = ['RS','SP','PR']
encode = {'RR':'a', 'RP':'b', 'RS':'c', 'PR':'d', 'PP':'e', 'PS':'f', 'SR':'g', 'SP':'h', 'SS':'i'}
decode = {'a':'RR', 'b':'RP', 'c':'RS', 'd':'PR', 'e':'PP', 'f':'PS', 'g':'SR', 'h':'SP', 'i':'SS'}

numMeta = 3 #num of meta strategies for each predictor

if input=='': #first round; initialize everything
	output = input = random.choice('RPS')
	currSet = 0
	score = 0
	allMoves = '' #history of all moves made
	myMoves = ''
	hisMoves = ''
	
	#initialize strategies
	def alwaysRock():
		return 'R'
	def alwaysPaper():
		return 'P'
	def alwaysScissors():
		return 'S'
	def rand():
		return random.choice('RPS')
		
	#old version of hist, this one does reverse search for a sequence of max length
	def hist_fwd_rvr(allMoves):
		toReturn1 = random.choice('abcdefghi')
		toReturn2 = random.choice('abcdefghi')
		
		lam = len(allMoves)
		maxDepth = 100
		maxLength = 10
		#search forwards strings of decreasing length
		l = min(maxLength,lam-1)
		foundAt = -1
		while l>0 and foundAt==-1:
			foundAt = allMoves.find(allMoves[lam-l:lam],0,lam-1)
			if foundAt == -1:
				l -= 1
		#Post condition: l is length of best match found, foundAt is its start point (if not -1)
		if foundAt != -1:
			toReturn1=allMoves[foundAt+l]
			#print "found sequence: " + allMoves[foundAt:foundAt+l]
			#print "your next move: " + decode[allMoves[foundAt+l]][1]
			
		#search backwards strings of decreasing length
		l = min(maxLength,lam-1)
		foundAt = -1
		while l>0 and foundAt==-1:
			foundAt = allMoves.rfind(allMoves[lam-l:lam],0,lam-1)
			if foundAt == -1:
				l -= 1
		if foundAt != -1:
			toReturn2=allMoves[foundAt+l]
		
		return toReturn1+toReturn2

	stored = ''
	def histFAll1():
		global allMoves,stored
		stored = hist_fwd_rvr(allMoves)
		return decode[stored[0]][0]
	def histFAll2():
		global stored
		return decode[stored[0]][1]
	def histRAll1():
		global stored
		return decode[stored[1]][0]
	def histRAll2():
		global stored
		return decode[stored[1]][1]
		
	histAnalysis = defaultdict(list)
	considerLengths = [3,4]
	histResults = ['']*len(considerLengths)
	def hist(allMoves,considerLengths): 
		global histAnalysis,histResults
		lam = len(allMoves)-1
		#learn from previous example
		keys = []
		for l in considerLengths:
			if lam < l: #can't learn this history
				keys.append('')
				continue
			key = allMoves[-l-1:-1]
			histAnalysis[key] += [allMoves[-1]]
			keys.append(key)
		#make predictions
		for i in xrange(len(considerLengths)):
			if lam < considerLengths[i]: #key will not be valid
				histResults[i] = random.choice('abcdefghi')
				continue
			key = keys[i]
			cand = histAnalysis[key]
			k = xrange(len(cand))
			k = max(random.choice(k),random.choice(k))
			histResults[i] = cand[k]
		
	#does history matching of length 3 (or whatever considerLengths[0] is)
	def hist1_1():
		global allMoves,considerLengths,histResults,decode
		hist(allMoves,considerLengths)
		return decode[histResults[0]][0]
	
	#history matching of length 3 (or whatever considerLenghts[0] is), but assumes they're using predictor against you
	def hist1_2():
		global histResults,decode
		return decode[histResults[0]][1]
	def hist2_1():
		global histResults,decode
		return decode[histResults[1]][0]
	def hist2_2():
		global histResults,decode
		return decode[histResults[1]][1]
		
	frq = [0,0,0]
	def freq1(): #predicts they will make the move they make most often
		global allMoves,frq,decode
		#learn from last move made
		if len(allMoves)==0:
			return 'X'
		frq[ 'RPS'.index(decode[allMoves[-1]][1]) ] += 1
		return 'RPS'[frq.index(max(frq))]
			
	frq2 = [0,0,0]
	def freq2(): #like freq, but assumes they think we're playing with freq and they want to beat it
		global allMoves,frq2,decode
		#learn from last move made
		if len(allMoves)==0:
			return 'X'
		frq2[ 'RPS'.index(decode[allMoves[-1]][0]) ] += 1
		return 'PSR'[frq2.index(max(frq2))]
		
	
	allStrats = [freq1,freq2,hist1_1,hist1_2,hist2_1,hist2_2,histFAll1,histFAll2,histRAll1,histRAll2,rand]
	allScores = [0]*len(allStrats)*numMeta
	allPredictions = ['X']*len(allStrats)*numMeta
	#for metameta level:
	mmScor = 0
	mmPred = 'X'
else:
	allMoves = allMoves + encode[output + input]
	myMoves = myMoves + output
	hisMoves = hisMoves + input
	scoreChange = 0
	if (output+input) in wins:
		score += 1
		scoreChange = 1
	elif (input+output) in wins:
		score -= 1
		scoreChange = -1
	else:
		score = 0
		scoreChange = 0
	
	if currSet >= 500 and score < 0:
		output = random.choice(['R','P','S']) #resort to random strategy
	else: #actually try something
		beat = {'R':'P', 'P':'S', 'S':'R', 'X':random.choice('RPS')}
		for i in xrange(len(allStrats)):
			for j in xrange(numMeta*i, numMeta*i+3):
				allScores[j] *= 0.85#max(0,allScores[j]-1) #decay
				mmScor *= 0.85#max(0,mmScor-1)
				if allPredictions[j] == input:
					allScores[j] += 10
				elif allPredictions[j] == beat[input]: #this prediction led to a loss, punish
					allScores[j] -= 10
				if mmPred == input:
					mmScor += 2
			predBase = allStrats[i]() #update predictions:
			jumpUp = {'R':'S', 'P':'R', 'S':'P', 'X':random.choice('RPS')}
			nmi = numMeta*i
			allPredictions[nmi] = predBase #P.0 : assume they'll follow the move exactly predicted
			allPredictions[nmi+1] = jumpUp[predBase] #P.1 - assume they predict we'll try to beat predBase
			allPredictions[nmi+2] = jumpUp[jumpUp[predBase]] #P.2 - assume they predict we'll try to beat jumpUp[predBase]
		
		#select the best one deterministically method 1: all who have max score, choose one randomly
		mx = max(allScores)
		i = random.choice([j for j in xrange(len(allScores)) if allScores[j]==mx])
		
		#check if metameta level is better
		output = beat[allPredictions[i]]
		mmPred = beat[output]
		if mmScor > allScores[i]:
			output = mmPred
		if output=='X':
			output = random.choice('RPS')
	
currSet += 1