import random

# first move setup
if input == "":
		
	last3Patterns = ['RRR', 'RRP', 'RRS', 'RPR', 'RPP', 'RPS', 'RSR', 'RSP', 'RSS', 'PRR', 'PRP', 'PRS', 'PPR', 'PPP', 'PPS', 'PSR', 'PSP', 'PSS', 'SRR', 'SRP', 'SRS', 'SPR', 'SPP', 'SPS', 'SSR', 'SSP', 'SSS']
	last3PatternsCounts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	

	thirdLastInput = "P"
	secondLastInput = "P"
	
	output = 'P'
	
	predictorscore=[1.2,0.7,0.7,0.6]
	predictors=['P','P','P','P']
	

	
# ready to go
else:
	
	# Score last predictors
	for i in range(4):
		predictorscore[i]*=0.87
		if input==predictors[i]:
			predictorscore[i]+=0.11
		elif input=={'R':'S', 'P':'R', 'S':'P'}[predictors[i]]:
			predictorscore[i]-=0.10
		else:
			predictorscore[i]-=0.03
	
	
	
	#Predictor 1: Random Predictors

	predictors[0]=random.choice(['R','P','S'])

	
	#Predictor 2-4 - 3 pattern macher
	
	last3PatternsCounts[last3Patterns.index(input + secondLastInput + thirdLastInput)]+=1
	
	sum = 0
	for i in range(27):
		sum+=last3PatternsCounts[i]
	
	averageWeight = sum / 27
	
	for i in range(1, 4):
	
		rWeight = last3PatternsCounts[last3Patterns.index("R" + input + secondLastInput)]
		pWeight = last3PatternsCounts[last3Patterns.index("P" + input + secondLastInput )]
		sWeight = last3PatternsCounts[last3Patterns.index("S" + input + secondLastInput )]
	
		if rWeight > pWeight and rWeight > sWeight and rWeight >= averageWeight:
			predictors[i] = "R"
	
		elif pWeight > rWeight and pWeight > sWeight and pWeight >= averageWeight:
			predictors[i] = "P"
	
		elif sWeight > pWeight and sWeight > rWeight and sWeight >= averageWeight:
			predictors[i] = "S"

		elif sWeight == pWeight and sWeight > rWeight and sWeight >= averageWeight:
			predictors[i]=random.choice(['P','S'])

		elif sWeight == rWeight and sWeight > pWeight and sWeight >= averageWeight:
			predictors[i]=random.choice(['R','S'])
		
		elif pWeight == rWeight and pWeight > sWeight and pWeight >= averageWeight:
			predictors[i]=random.choice(['R','P'])
		
		else:
			predictors[i]=random.choice(['R','P','S'])

		



	#compare predictors
	best = 0
	
	for i in range(4):
		if predictorscore[i]>best:
			output = {'R':'P','P':'S','S':'R'}[predictors[i]]
			best = predictorscore[i]
			
			
	thirdLastInput = secondLastInput
	secondLastInput = input