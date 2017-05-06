import random

# first move setup
if input == "":
		
	lastInputsPatterns = ['RRR', 'RRP', 'RRS', 'RPR', 'RPP', 'RPS', 'RSR', 'RSP', 'RSS', 'PRR', 'PRP', 'PRS', 'PPR', 'PPP', 'PPS', 'PSR', 'PSP', 'PSS', 'SRR', 'SRP', 'SRS', 'SPR', 'SPP', 'SPS', 'SSR', 'SSP', 'SSS']
	lastInputsPatternsOccurences = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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
	
	
	
		
	sum = 0
	for i in range(27):
		sum+=lastInputsPatternsOccurences[i]
	
	averageWeight = sum / 27
	
	lastInputsPatternsOccurences[lastInputsPatterns.index(input + secondLastInput + thirdLastInput)]+=1

	rWeight = lastInputsPatternsOccurences[lastInputsPatterns.index("R" + input + secondLastInput)]
	
	pWeight = lastInputsPatternsOccurences[lastInputsPatterns.index("P" + input + secondLastInput )]
	
	sWeight = lastInputsPatternsOccurences[lastInputsPatterns.index("S" + input + secondLastInput )]	
		
	if rWeight > pWeight and rWeight > sWeight and rWeight >= averageWeight :
		pridictedInput = "R"
	
	elif pWeight > rWeight and pWeight > sWeight and pWeight >= averageWeight :
		pridictedInput = "P"
	
	elif sWeight > pWeight and sWeight > rWeight and sWeight >= averageWeight :
		pridictedInput = "S"

	elif sWeight == pWeight and sWeight > rWeight and sWeight >= averageWeight :
		pridictedInput =random.choice(['P','S'])

	elif sWeight == rWeight and sWeight > pWeight and sWeight >= averageWeight :
		pridictedInput=random.choice(['R','S'])
		
	elif pWeight == rWeight and pWeight > sWeight and pWeight >= averageWeight :
		pridictedInput=random.choice(['R','P'])
		
	else:
		pridictedInput=random.choice(['R','P','S'])

	
	output = {'R':'P','P':'S','S':'R'}[pridictedInput]
	
	thirdLastInput = secondLastInput
	secondLastInput = input