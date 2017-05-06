import random

if input == "":
	# first time, initialize variables
	wins = ['RS', 'SP', 'PR']
	isDebug = False
	shouldRandom = True
	
	_scaleFactor = 1 # 1-10 : 0.1
	_decayFactor = 0.9 # 0.1 - 1 : 0.1
	_confidenceFactor = 0 # -inf - inf : 0.1
	
	myPlay = ''
	hisPlay = ''
	myScore = ''
	predictorPlay = []
	predictorScore = []
else:
	# record opponent play
	hisPlay += input
	# get my last play
	output = myPlay[-1]
	# determine scoring
	if (output+input) in wins:
		myScore += '2'
	elif (input+output) in wins:
		myScore += '0'
	else:
		myScore += '1'
	# update predictors with past move
	nList = [5,4,3,2]
	for N in nList:
		if len(hisPlay) >= N+1:
			nP = getLastNPlay(N, hisPlay)
			print nP
			# if predictor already contains our past play, update predictor
			if nP in predictorPlay:
				i = predictorPlay.index(nP)
				# update score with decay factor and score
				predictorScore[i] *= _decayFactor
				predictorScore[i] += int(myScore[-1]) - 1
			# if first time, initialize our past play into predictor
			else:
				predictorPlay.append(nP)
				finalS = _scaleFactor*(float(myScore[-1])-1)
				predictorScore.append(finalS)
	# if less than 10 times played, return random
	if len(myPlay) <= 9:
		# return random
		shouldRandom = True
	else:
		nList = [5,4,3,2]
		# generate our best estimated play
		for N in nList:
			nP = getLastNPlay(N-1, hisPlay)
			tmpScore = []
			letterCase = ['R','P','S']
			for letter in letterCase:
				tmpP = nP
				tmpP += letter
				if tmpP in predictorPlay:
					i = predictorPlay.index(tmpP)
					tmpScore.append(predictorScore[i])
				else:
					tmpScore.append(-99999)
			maxScore = max(tmpScore)
			if maxScore >= _confidenceFactor:
				shouldRandom = False;
				i = tmpScore.index(maxScore)
				if isDebug:
					print 'predict next play: ' + nP + letterCase[i]
				output = beatIt(letterCase[i])
			else:
				if isDebug:
					print 'random in effect'
				shouldRandom = True;

if shouldRandom:
	output = random.choice(['R','P','S'])
if isDebug:
	print 'hisPlay:' + hisPlay
	print 'myPlay: ' + myPlay
	print 'predictorScore: ' + '-'.join('%0.2f'%num for num in predictorScore)
	#print 'predictorScore: ' + '-'.join(str(num) for num in predictorScore)
	#print ['%0.2f' % num for num in predictorScore]
	print 'predictorPlay:  ' + '- '.join(predictorPlay)
	print '**************'
# record our play
myPlay += output

def getLastNPlay(n, data):
	return data[len(data)-n-1:]

def beatIt(play):
	if play == 'R':
		return 'P'
	elif play == 'P':
		return 'S'
	elif play == 'S':
		return 'R'
	else:
		return 'X'