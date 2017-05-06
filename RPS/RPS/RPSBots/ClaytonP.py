import random

# first move setup
if input == "":
		
	last3Patterns = ['RRR', 'RRP', 'RRS', 'RPR', 'RPP', 'RPS', 'RSR', 'RSP', 'RSS', 'PRR', 'PRP', 'PRS', 'PPR', 'PPP', 'PPS', 'PSR', 'PSP', 'PSS', 'SRR', 'SRP', 'SRS', 'SPR', 'SPP', 'SPS', 'SSR', 'SSP', 'SSS']
	last3PatternsCounts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	

	thirdLastInput = "P"
	secondLastInput = "P"
	
	output = 'P'
	
	predictorscore=[1.2,0.7,0.7,0.6,0.6,0,0,0,0,]
	predictors=['P','P','P','P','P','P','P','P','P']
	

	
# ready to go
else:
	
	# Score last predictors
	for i in range(9):
		predictorscore[i]*=0.87
		if input==predictors[i]:
			predictorscore[i]+=0.11
		elif input=={'R':'S', 'P':'R', 'S':'P'}[predictors[i]]:
			predictorscore[i]-=0.10
		else:
			predictorscore[i]-=0.03
	
	
	
	#Predictor 0-2: Random Predictors
	for i in range(3):
		predictors[i]=random.choice(['R','P','S'])

	
	#Predictor 3-5 - 3 pattern macher
	
	last3PatternsCounts[last3Patterns.index(input + secondLastInput + thirdLastInput)]+=1
	
	for i in range(3, 6):
	
		rWeight = last3PatternsCounts[last3Patterns.index("R" + input + secondLastInput)]
		pWeight = last3PatternsCounts[last3Patterns.index("P" + input + secondLastInput )]
		sWeight = last3PatternsCounts[last3Patterns.index("S" + input + secondLastInput )]
	
		if rWeight > pWeight and rWeight > sWeight :
			pridictedInput = "R"
	
		elif pWeight > rWeight and pWeight > sWeight:
			pridictedInput = "P"
	
		elif sWeight > pWeight and sWeight > rWeight:
			pridictedInput = "S"

		elif sWeight == pWeight and sWeight > rWeight:
			pridictedInput=random.choice(['P','S'])

		elif sWeight == rWeight and sWeight > pWeight:
			pridictedInput=random.choice(['R','S'])
		
		elif pWeight == rWeight and pWeight > sWeight:
			pridictedInput=random.choice(['R','P'])
		
		else:
			pridictedInput=random.choice(['R','P','S'])

		predictors[i] = {'R':'P','P':'S','S':'R'}[pridictedInput]


	#Predictor 3-5 - inverse 3 pattern macher
	for i in range(6, 9):
		predictors[i] = {'R':'P','P':'S','S':'R'}[predictors[i - 3]]




	#compare predictors
	best = 0
	
	for i in range(9):
		if predictorscore[i]>best:
			output = predictors[i]
			best = predictorscore[i]
			
			
	thirdLastInput = secondLastInput
	secondLastInput = input