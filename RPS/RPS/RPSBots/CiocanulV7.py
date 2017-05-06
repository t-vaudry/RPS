import random

input  = ""
output = ""

#Trace for the entire match, pairs (My choice, His Choice, +-1 I won)
#trace  = [("R","P",1),("R","P",1),("R","P",1),("R","P",1),("R","P",1),("R","P",1),("R","P",1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",1),("R","P",1),("R","P",1),("R","P",1),("R","P",-1)]
trace = []
#they each vote on the next move to make
traceTemp=[]

#(Vote cast, Which Trace, Confidence)
votes      =[("N",0,0.0),("N",0,0.0),("N",0,0.0),("N",0,0.0),("N",0,0.0)]

def didIWin():
	if(output == input):
		return (output, input, 0)
	elif(output == "R" and input == "S"):
		return ("R","S",1)
	elif(output == "R" and input == "P"):
		return ("R","P",-1)
	elif(output == "P" and input == "S"):
		return ("P","S",-1)
	elif(output == "P" and input == "R"):
		return ("P","R",1)
	elif(output == "S" and input == "R"):
		return ("S","R",-1)
	elif(output == "S" and input == "P"):
		return ("S","P",-1)
	return ("R","P",1)


#traceOffset - from which idx of the trace do we start
#step        - the step, every 1 tuple, every 2, etc
#minTraces   - the minimum number of states this tempTrace can contain
#maxTraces   - the maximum number of states this tempTrace can contain
def buildTraceTemp(traceOffset, step, minTrace, maxTrace):
	del traceTemp[:]

	if(traceOffset < 0):
		traceOffset = 0

	#get the number of correct traces we have
	traceCount  = len(trace) - traceOffset

	#make a decision when all of them are able to
	if(traceCount >= minTrace):
		k = 0 #counter
		i = 0 #idx in the trace
		traceExhausted = False

		i = traceOffset

		while (k<= maxTrace and not traceExhausted):
			traceTemp.append(trace[i])
			i = i+step
			k = k+1
			if(k*step + step >= traceCount):
				traceExhausted = True #need to leave an extra valua for the decision			

		#we now have the trace, compare it against the last 
		similarity = 0
		#get the similiraties beween the traceTemp and the realTrace
		if (traceExhausted== True):
			k = traceCount
		similarity = similarityBetween(traceTemp,trace[traceOffset:traceOffset+k])

		#make it a percentage 
		similarity = similarity / (k-1)

		#if they were exactly similar, cast a 'bigger' vote
		if (similarity==1.0):
			similarity = 3

		#now cast our vote
		result = trace[k*step]

		#if we won with that choice
		if(result[2] == 1):
			#return what we voted then, and confidence
			votes.append((result[0],similarity))
		#or we drew it
		elif(result[2]==0):
			votes.append(("R", similarity/3))
			votes.append(("P", similarity/3))
			votes.append(("S", similarity/3))
		#or we lost it
		else:
			twoVotes = reverseVotes(result[0])
			votes.append((twoVotes[0], 1 - similarity/2))
			votes.append((twoVotes[1], 1 - similarity/2))
	else:
		votes.append(("N",1))

#assumes they have the same length
def similarityBetween(a,b):
	k = 0 #counter
	similarity = 0
	while(k<len(a)):
		if(a[k] == b[k]):
			similarity +=1
		k = k+1
	return similarity
 	
def reverseVotes(v):
	if v == "R":
		return ("P","S")
	elif v == "P":
		return ("R","S")
	else:
		return ("R","P")
	return "N"
	
	

if input == "": #first round, return a random variable
	output = random.choice(["R","P","S"])
	print "Random init vote "
	print output
else:
	print "INIT"
	del votes[:]
	trace.append(didIWin())
	
	#buildTraceTemp(traceOffset, step, minTrace, maxTrace):
	currLen = len(trace)
	step = 1
	for lengthToCheck in [4,5]:
		#middle early early values of the original trace
		randomness = random.randint(int(currLen*0.1), int(currLen*0.3))
		buildTraceTemp(currLen/2 - 2*lengthToCheck*step- randomness, step, 4, lengthToCheck)
		#middle early values of the original trace
		randomness = random.randint(int(currLen*0.1), int(currLen*0.3))
		buildTraceTemp(currLen/2 - lengthToCheck*step  - randomness, step, 4, lengthToCheck)
		#middle late values of the original trace
		randomness = random.randint(int(currLen*0.1), int(currLen*0.3))
		buildTraceTemp(currLen/2 + lengthToCheck*step  + randomness, step, 4, lengthToCheck)
		#middle late late values of the original trace
		randomness = random.randint(int(currLen*0.1), int(currLen*0.3))
		buildTraceTemp(currLen/2 + 2*lengthToCheck*step+ randomness, step, 4, lengthToCheck)
		#last games
		randomness = random.randint(int(currLen*0.1), int(currLen*0.3))
		buildTraceTemp(currLen - lengthToCheck*step - randomness, step, 4, lengthToCheck)
	
	rockCount = paperCount = scissorsCount = noneCount= 0.0
	#count the votes
	for v in votes:
		#check the vote
		if  (v[0]=="R"):
			rockCount +=  v[1] #add the confidence level
		elif (v[0]=="P"):
			paperCount += v[1]
		elif (v[0]=="S"):
			scissorsCount +=v[1]
		else:
			noneCount +=1

	#return a non-random answer	if we have enough confidence level
	if(noneCount < rockCount + paperCount + scissorsCount):
		if rockCount > paperCount and rockCount > scissorsCount:
			output = random.choice(["P","S"])
			#output = "R" 
		elif paperCount > scissorsCount:
			#output = "P"
			output = random.choice(["R","S"])
		else:
			#output = "S"
			output = random.choice(["R","P"])
	else:
		output = random.choice(["R","P","S"])