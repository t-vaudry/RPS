from math   import *
from random import *
from copy   import deepcopy

LOOK_BACK_DIST = 8
HIST_SIZE = 16
R, P, S        = 0, 1, 2
MINE, HIS      = 0, 1 
RPSmaps        = {R:'R', P:'P', S:'S', 'R':R,   'P':P,   'S':S}
RPSbeats       = {'R':'S', 'P':'R', 'S':'P', R:'S', P:'R', S:'P'}
RPSPairs       = {'RR':0, 'RP':0, 'RS':0,
                  'PR':0, 'PP':0, 'PS':0,
                  'SR':0, 'SP':0, 'SS':0}
                  
def getBestRPS(RPSFreq):
	bestx = 0
	for x in range(0, len(RPSFreq)):
		if(RPSFreq[x] > RPSFreq[bestx]):
			bestx = x
	return RPSmaps[bestx]
	
def getFreqPredict(RPSFreq):
	return RPSbeats[getBestRPS(RPSFreq)]
	
def getLookBackPredict(relHist, lookback):
	RPSGuessWeights = [0,0,0]
	for x in range(1, len(lookback)):
		for y in range(0, len(relHist)):
			lookBackSub = lookback[(-1*x):]
			histSub = relHist[y:(y + len(lookBackSub))]
			if(histSub == lookBackSub and y < len(relHist)-1):
				RPSGuessWeights[RPSmaps[relHist[y+1]]] += pow(2, x)
				#print RPSGuessWeights
	return RPSbeats[getBestRPS(RPSGuessWeights)]
	
def getHennyPredict(relHist):
	return RPSbeats[relHist[randint(0, len(relHist)-1)]]
	
def getPairPredict(myMove, pairs):
	rps = "RPS"
	freq = [0,0,0]
	for x in range(0, len(rps)):
		tmp = myMove + rps[x]
		freq[x] = pairs[tmp]
	return RPSbeats[getBestRPS(freq)]
	
def getMove(sideFreq, sideHist, lookback, pairs):
	moveOptions = [0,0,0]
	hennyPredict    = getHennyPredict(sideHist)
	freqPredict     = getFreqPredict(sideFreq)
	lookbackPredict = getLookBackPredict(sideHist, lookback)
	
	moveOptions[RPSmaps[hennyPredict   ]] += 2
	moveOptions[RPSmaps[freqPredict    ]] += 3
	moveOptions[RPSmaps[lookbackPredict]] += 5
	
	pairPredict = getPairPredict(getBestRPS(moveOptions), pairs)
	
	moveOptions[RPSmaps[pairPredict]] += 7
	
	return moveOptions
if(input == ""):       
	RPSMyPairGame    = deepcopy(RPSPairs)
	RPSEnemyPairGame = deepcopy(RPSPairs)
	
	RPSGameHist = ["", ""]
	RPSLookBack = ["", ""]
	
	RPSEnemyCounts = [0,0,0]
	EnemyHist = ""
	
	RPSMyCounts = [0,0,0]
	MyHist = ""
	
	output = choice("RPS")
else:
	#Update my info
	MyHist += output
	MyHist = MyHist[-HIST_SIZE:]
	RPSGameHist[MINE] += (input + output)
	RPSMyCounts[RPSmaps[output]] += 1
	RPSMyPairGame[(input + output)] += 1
	
	#Update the enemy info
	EnemyHist += input
	EnemyHist = EnemyHist[-HIST_SIZE:]
	RPSGameHist[HIS] += (output + input)
	RPSEnemyCounts[RPSmaps[input]] += 1
	RPSEnemyPairGame[(output + input)] += 1
	
	#Update the lookbacks
	RPSLookBack[MINE] = EnemyHist[-LOOK_BACK_DIST:]
	RPSLookBack[HIS]  = MyHist[-LOOK_BACK_DIST:]
	
	myMoves  = getMove(RPSEnemyCounts, EnemyHist, RPSLookBack[MINE],  RPSEnemyPairGame)
	hisMoves = getMove(RPSMyCounts,    MyHist,    RPSLookBack[HIS], RPSMyPairGame)
	finalMoves = [0,0,0]
	for x in range(0, len(finalMoves)):
		finalMoves[x] = myMoves[x] - hisMoves[x]*.75
	output = RPSbeats[getBestRPS(finalMoves)]