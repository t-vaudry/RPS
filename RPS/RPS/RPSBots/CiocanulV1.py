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
	if(output == "R" and input == "S"):
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


#how many items to they need in trace before they can start their thing
minTraces=[5,10,15,20,25]
#how many items can each special trace have
maxTraces=[10,10,10,10,10]

#compare the special traces against the X last characters
lengthCompare = 10
	
#just get the last X values
def buildTraceTemp(traceNo):
	#ignore the last 10 values, as we use those to compare this tempTrace against
	traceCount  = len(trace) - lengthCompare

	del traceTemp[:]
	#make a decision when all of them are able to
	if(traceCount >= max(minTraces)):
		k = 0 #counter
		i = 0 #idx in the trace
		traceExhausted = False
		step = 1+traceNo

		if(traceCount < maxTraces[traceNo]*step):
			#then start from the start of the trace
			i = 0
		else:
			i = traceCount - maxTraces[traceNo]*step 
		
		while (k<= maxTraces[traceNo] and not traceExhausted):
			traceTemp.append(trace[i])
			i = i+step
			k = k+1
			if(k*step + step >= minTraces[traceNo]):
				traceExhausted = True #need to leave an extra valua for the decision			

		#we now have the trace, compare it against the last 
		similarity = 0
		if(k>lengthCompare):
			#get the last lengthCompare elements
			similarity = len(set(traceTemp[k-lengthCompare-1:]) & set(trace[traceCount-lengthCompare-1:]))			
			#make it a percentage 
			similarity = similarity / lengthCompare
		else:
			#get the last k components
			similarity = len(set(traceTemp) & set(trace[traceCount-k-1:]))
			#make it a percentage 
			similarity = similarity / k		

		#now cast our vote
		result = trace[k*step]

		#if we won with that choice
		if(result[2] == 1):
			#return what we voted then, our id, and confidence
			votes.append((result[0],traceNo,similarity))
		else:
			twoVotes = reverseVotes(result[0])
			votes.append((twoVotes[0],traceNo, 1 - similarity/2))
			votes.append((twoVotes[1],traceNo, 1 - similarity/2))
	else:
		votes.append(("N",traceNo,1))

		
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
	
	for i in range(0,5):
		buildTraceTemp(i)

	rockCount = paperCount = scissorsCount = noneCount= 0.0
	#count the votes
	for v in votes:
		#check the vote
		if  (v[0]=="R"):
			rockCount +=  v[2] #add the confidence level
		elif (v[0]=="P"):
			paperCount += v[2]
		elif (v[0]=="S"):
			scissorsCount +=v[2]
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