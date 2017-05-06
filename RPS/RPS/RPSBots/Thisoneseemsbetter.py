from math   import *
from random import *

LOOK_BACK_DIST = 12
HIST_SIZE = 45
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
		if(RPSFreq[x] >= RPSFreq[bestx]):
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
	
	#moveOptions[RPSmaps[hennyPredict   ]] += 2
	moveOptions[RPSmaps[freqPredict    ]] += 3
	moveOptions[RPSmaps[lookbackPredict]] += 5
	
	#pairPredict = getPairPredict(getBestRPS(moveOptions), pairs)
	
	#moveOptions[RPSmaps[pairPredict]] += 7
	
	return moveOptions
if(input == ""):       
	RPSMyPairGame    = RPSPairs
	
	RPSGameHist = ""
	RPSLookBack = ""
	
	RPSMyCounts = [0,0,0]
	MyHist = ""
	
	output = choice("RPS")
else:
	#Update my info
	MyHist += input
	MyHist = MyHist[-HIST_SIZE:]
	RPSGameHist += (input + output)
	RPSMyCounts[RPSmaps[input]] += 1
	RPSMyPairGame[(input + output)] += 1
	
	RPSLookBack = MyHist[-LOOK_BACK_DIST:]
	
	myMoves = getMove(RPSMyCounts, MyHist, RPSLookBack,  RPSMyPairGame)
	output = RPSbeats[getBestRPS(myMoves)]