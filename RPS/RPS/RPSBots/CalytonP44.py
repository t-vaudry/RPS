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
		
	if rWeight > pWeight and rWeight > sWeight and rWeight >= averageWeight and rWeight - pWeight > rWeight * 0.5 and rWeight - sWeight > rWeight * 0.5:
		pridictedInput = "R"
	
	elif pWeight > rWeight and pWeight > sWeight and pWeight >= averageWeight and pWeight - rWeight > pWeight * 0.5 and pWeight - sWeight > pWeight * 0.5 :
		pridictedInput = "P"
	
	elif sWeight > pWeight and sWeight > rWeight and sWeight >= averageWeight and sWeight - pWeight > sWeight * 0.5 and sWeight - rWeight > sWeight * 0.5:
		pridictedInput = "S"

	elif sWeight == pWeight and sWeight > rWeight and sWeight >= averageWeight and sWeight - rWeight > sWeight * 0.5:
		pridictedInput =random.choice(['P','S'])

	elif sWeight == rWeight and sWeight > pWeight and sWeight >= averageWeight and rWeight - pWeight > rWeight * 0.5:
		pridictedInput=random.choice(['R','S'])
		
	elif pWeight == rWeight and pWeight > sWeight and pWeight >= averageWeight and rWeight - sWeight > rWeight * 0.5:
		pridictedInput=random.choice(['R','P'])
		
	else:
		pridictedInput=random.choice(['R','P','S'])

	
	output = {'R':'P','P':'S','S':'R'}[pridictedInput]
	
	thirdLastInput = secondLastInput
	secondLastInput = input