import random

input  = ""
output = ""

#Trace for the entire match, pairs (My choice, His Choice, +-1 I won)
#trace  = [("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1),("R","P",-1)]
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

	#get the number of correct traces we have
	traceCount  = len(trace) - traceOffset

	#make a decision when all of them are able to
	if(traceCount >= minTraces):
		k = 0 #counter
		i = 0 #idx in the trace
		traceExhausted = False

		if(traceCount < maxTrace*step):
			#then start from the start of the trace
			i = 0
		else:
			i = traceCount - maxTrace*step 
		
		while (k<= maxTrace and not traceExhausted):
			traceTemp.append(trace[i])
			i = i+step
			k = k+1
			if(k*step + step >= minTrace):
				traceExhausted = True #need to leave an extra valua for the decision			

		#we now have the trace, compare it against the last 
		similarity = 0
		#get the k similiraties beween the traceTemp and the realTrace
		similarity = len(set(traceTemp) & 
						 set(trace[traceOffset:traceOffset+k]))
		#make it a percentage 
		similarity = similarity / k		

		#now cast our vote
		result = trace[k*step]

		#if we won with that choice
		if(result[2] == 1):
			#return what we voted then, and confidence
			votes.append((result[0],similarity))
		#or we drew it
		elif(result[2]==0):
			votes.append(("R", 0.33))
			votes.append(("P", 0.33))
			votes.append(("S", 0.33))
		#or we lost it
		else:
			twoVotes = reverseVotes(result[0])
			votes.append((twoVotes[0], 1 - similarity/2))
			votes.append((twoVotes[1], 1 - similarity/2))
	else:
		votes.append(("N",1))

		
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
	trace.append(didIWin)
	
	#buildTraceTemp(traceOffset, step, minTrace, maxTrace):
	currLen = len(trace)
	
	for lengthToCheck in [10,20]:
		for step in range(1,3):
			#middle early early values of the original trace
			buildTraceTemp(curLen/2 - 2*lengthToCheck*step, step, 5, lengthToCheck)
			#middle early values of the original trace
			buildTraceTemp(curLen/2 - lengthToCheck*step, step, 5, lengthToCheck)
			#middle late values of the original trace
			buildTraceTemp(curLen/2 + lengthToCheck*step, step, 5, lengthToCheck)
			#middle late late values of the original trace
			buildTraceTemp(curLen/2 + 2*lengthToCheck*step, step, 5, lengthToCheck)
			#last games
			buildTraceTemp(curLen - lengthToCheck*step, step, 5, lengthToCheck)
	
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
			output = "R" 
		elif paperCount > scissorsCount:
			output = "P"
		else:
			output = "S"
	else:
		output = random.choice(["R","P","S"])