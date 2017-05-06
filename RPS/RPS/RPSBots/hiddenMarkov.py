import random
import math
K =  10 # Number of Hidden states
E = 3 # Number of Evidence states R, P, S

def toInt(s):
	if s == 'R':
		return 0
	elif s == 'P':
		return 1
	elif s =='S':
		return 2

# initialize the parameters
startProb = [1.0 / K for h in range(K)]

transProb = [[1.0 / K for h2 in range(K)] for h1 in range (K)]

emitProb = [[1.0 / E for e in range(E)] for h in range (K)]

def normalize(weights):
	total = sum(weights)
	return [1.0 * w / total for weight in weights]

#for every position, give a distribution of hidden state
#forward-backward
#for every position, give a distribution of hidden state
def forwardBackward(observation, startProb, transProb, emitProb):
	n = len(observation)
	H = len(startProb)

	def weight(h1, h2, i):
		#weight on edge from (H_{i-1} = h1) to (H_i = h2)
		w = 1
		if i == 0:
			w *= startProb[h2]
		else:
			w *= transProb[h1][h2]
		w *= emitProb[h2][observation[i]]
		return w
	
	forward = [None] * n
	for i in range(n):
		forward[i] = [None] * H
		for h2 in range(H):
			if i == 0:
				forward[i][h2] = weight(None, h2, 0)
			else:
				forward[i][h2] = sum(forward[i - 1][h1] * weight(h1, h2, i) \
                               for h1 in range(H))
		forward[i] = normalize(forward[i])

	backward = [None] * n
	for i in range(n-1, -1, -1):
		backward[i] = [None] * H
		for h1 in range(H):
			if i == n - 1:
				backward[i][h1] = 1
			else:
				backward[i][h1] = sum(weight(h1, h2, i + 1) * backward[i + 1][h2] \
                              for h2 in range(H))
			backward[i] = normalize(backward[i])

	mu = [None] * n
	for i in range(n):
		mu[i] = [None] * H
		for h in range(H):
			mu[i][h] = forward[i][h] * backward[i][h]
		mu[i] = normalize(mu[i])
	return mu

def HMMInference(urgame):  #urgames is the training set we got
	#use EM to build the model
	observation = [toInt(s) for s in urgame]
	length = len(observation)
	mu = [[0 for k in range(K)] for n in range(length)]
	for t in range(200):
		#E - step
		mu = forwardBackward(observation, startProb, transProb, emitProb)

		#M-step
		startCounts = [0 for h in range(K)]
		emitCounts = [[0 for e in range(E)] for h in range (K)]
		transCounts = [[0 for h2 in range(K)] for h1 in range (K)]

		for i, probs in enumerate(mu):
			#update startCounts
			if i == 0:
				for h in range(K):
					startCounts[h] += probs[h]
			#update emission counts
			e = observations[i]
			for h in range(K):
				emitCounts[h][e] += probs[h]
			#update transion counts
			if i > 0:
				prevProbs = mu[i - 1]
				for h1 in range(K):
					for h2 in range(K):
						transCounts[h1][h2] += prevProbs[h1] * probs[h2]
		startProb = normalize(startCounts)
		for h in range(K):
			emitProb[h] = normalize(emitCounts[h])
			transProb[h] = normalize(transCounts[h])
	
	#based on the model predict the next output
	#compute the distribution of new hidden state
	newHidden = [0 for k in range(K)]
	for newH in range(K):
		newHidden[newH] = sum(transProb[h][newH] * mu[lenth - 1][h] for h in range(K))
	newHidden = normalize(newHidden)

	#conpute the distribution of new evidence state
	newEvidence = [0 for e in range(E)]
	for newE in range(E):
		newEvidence[newE] = sum(emitProb[h][newE] * newHidden[h] for h in range(K))
	newEvidence = normalize(newEvidence)

	#sample based on the weights
	key = random.uniform(0, 1)
	elements = ['R', 'P', 'S']
	runningTotal = 0.0
	chosen = None
	for i in range(K):
		weight = newEvidence[i]
		runningTotal += weight
		if runningTotal > key:
			chosen = elements[i]
	return chosen


#game play

myGameSeq = ""
urGameSeq = ""
if not input: 
    output = random.choice(['R', 'P', 'S'])
else:
    myGameSeq += output
    urGameSeq += input
    if len(myGameSeq) < 5:
    	output = random.choice(['R', 'P', 'S'])

    else:
        urgame = urGameSeq[-5:]
    	output = HMMInference(urgame)