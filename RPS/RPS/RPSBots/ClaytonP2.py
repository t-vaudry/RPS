import random

# first move setup
if input == "":
		
	lastInputsPatterns = ['RRR', 'RRP', 'RRS', 'RPR', 'RPP', 'RPS', 'RSR', 'RSP', 'RSS', 'PRR', 'PRP', 'PRS', 'PPR', 'PPP', 'PPS', 'PSR', 'PSP', 'PSS', 'SRR', 'SRP', 'SRS', 'SPR', 'SPP', 'SPS', 'SSR', 'SSP', 'SSS']
	lastInputsPatternsOccurences = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	
	thirdLastInput = ""
	secondLastInput = ""
	
	

# still building history
if secondLastInput == "" or thirdLastInput == "":
	output=random.choice(['R','P','S'])
	thirdLastInput = secondLastInput
	secondLastInput = input
	
# ready to go
else:

	
	
	lastInputsPatternsOccurences[lastInputsPatterns.index(input + secondLastInput + thirdLastInput)]+=1
	
	rWeight = pWeight = sWeight = 0
	
	rWeight = lastInputsPatternsOccurences[lastInputsPatterns.index(input + secondLastInput + "R")]
	
	pWeight = lastInputsPatternsOccurences[lastInputsPatterns.index(input + secondLastInput + "P")]
	
	sWeight = lastInputsPatternsOccurences[lastInputsPatterns.index(input + secondLastInput + "S")]
	
	if rWeight > pWeight and rWeight > sWeight:
		pridictedInput = "R"
	
	elif pWeight > sWeight:
		pridictedInput = "P"
	
	else:
		pridictedInput = "S"

	
	output = {'R':'P','P':'S','S':'R'}[pridictedInput]
	
	thirdLastInput = secondLastInput
	secondLastInput = input