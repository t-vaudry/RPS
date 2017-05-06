import random

# first move setup
if input == "":
		
	lastInputsPatterns = ['RRR', 'RRP', 'RRS', 'RPR', 'RPP', 'RPS', 'RSR', 'RSP', 'RSS', 'PRR', 'PRP', 'PRS', 'PPR', 'PPP', 'PPS', 'PSR', 'PSP', 'PSS', 'SRR', 'SRP', 'SRS', 'SPR', 'SPP', 'SPS', 'SSR', 'SSP', 'SSS']
	lastInputsPatternsOccurences = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	lastInputsPatternsOccurences = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	
	thirdLastInput = ""
	secondLastInput = ""
	rCount = pCount = sCount = 0
	rounds = 0
	
	

# still building history
if secondLastInput == "" or thirdLastInput == "" or rounds < 20:
	output=random.choice(['R','P','S'])
	thirdLastInput = secondLastInput
	secondLastInput = input
	rounds+=1
	
# ready to go
else:

	# set weights to 0	
	rWeight = pWeight = sWeight = 0
	
	
	# update input counts
	if input == "R":
		rCount += 1
	elif input == "P":
		pCount += 1
	elif input == "S":
		sCount += 1
	
	# if any input happens more then 50% of the time then assign a weight to it
	if rCount > rCount + pCount + sCount * (1/3):
		rWeight+= 1
	
	elif pCount > rCount + pCount + sCount * (1/3):
		pWeight+= 1
	
	elif sCount > rCount + pCount + sCount * (1/3):
		sWeight+= 1
	
	
	
	
	# update pattern occurences
	lastInputsPatternsOccurences[lastInputsPatterns.index(input + secondLastInput + thirdLastInput)]+=1
	

	
	# get the occurance counts of possible next inputs
	rockOccurrences = lastInputsPatternsOccurences[lastInputsPatterns.index("R" + input + secondLastInput)]
	
	paperOccurrences = lastInputsPatternsOccurences[lastInputsPatterns.index("P" + input + secondLastInput )]
	
	scissorsOccurrences = lastInputsPatternsOccurences[lastInputsPatterns.index("S" + input + secondLastInput )]
	
	# if any occurance count is greater then 50% then assign a weight to the corrisponding input
	if rockOccurrences > rockOccurrences + paperOccurrences + scissorsOccurrences * (1/3):
		rWeight+= 2
	
	elif paperOccurrences > rockOccurrences + paperOccurrences + scissorsOccurrences * (1/3):
		pWeight+= 2
	
	elif scissorsOccurrences > rockOccurrences + paperOccurrences + scissorsOccurrences * (1/3):
		sWeight+= 2
		
	
	
		
		
		
	#if the weight of any possible input is greater then the others then set it to the predicted input
	#if not - go random
	if rWeight > pWeight and rWeight > sWeight:
		pridictedInput = "R"
	
	elif pWeight > rWeight and pWeight > sWeight:
		pridictedInput = "P"
	
	elif sWeight > pWeight and sWeight > rWeight:
		pridictedInput = "S"
		
	else:
		pridictedInput=random.choice(['R','P','S'])

	
	output = {'R':'P','P':'S','S':'R'}[pridictedInput]
	
	thirdLastInput = secondLastInput
	secondLastInput = input