import random, operator
SIZE = 12
NOP = 7

if input == "":
	RPS = ["R","P","S"]
	STRATEGY = ["R","P","S","r1","r2","r3","EneMostPlayed","EneLeastPlayed","MyMostPlayed","MyLeastPlayed","Input-0","Input-1","Input-2","Input-3","Input-4","Input-5","Input-6","Input-7","Input-8","Input-9","Input-10","Input-11","Input-12","Output-0","Output-1","Output-2","Output-3","Output-4","Output-5","Output-6","Output-7","Output-8","Output-9","Output-10","Output-11","Output-12"]
	
	PREDICTORS = {"r1" : "","r2" : "","r3" : "","R" : "","P" : "","S" : "","EneMostPlayed" : "", "EneLeastPlayed" : "", "MyMostPlayed" : "", "MyLeastPlayed" : "" , "Input-0" : "", "Input-1" : "", "Input-2" : "", "Input-3" : "","Input-4" : "","Input-5" : "","Input-6" : "","Input-7" : "","Input-8" : "","Input-9" : "","Input-10" : "","Input-11" : "","Input-12" : "", "Output-0" : "", "Output-1" : "", "Output-2" : "", "Output-3" : "","Output-4" : "","Output-5" : "","Output-6" : "","Output-7" : "","Output-8" : "","Output-9" : "","Output-10" : "","Output-11" : "","Output-12" : ""}	
	
	PREDICTOR_SCORE = {"r1" : 1,"r2" : 1,"r3" : 1,"R" : 1,"P" : 1,"S" : 1,"EneMostPlayed" : 1, "EneLeastPlayed" : 1,  "MyMostPlayed" : 1, "MyLeastPlayed" : 1 , "Input-0" : 1, "Input-1" : 1,"Input-2" : 1, "Input-3" : 1 ,"Input-4" : 1,"Input-5" : 1,"Input-6" : 1,"Input-7" : 1,"Input-8" : 1,"Input-9" : 1,"Input-10" : 1,"Input-11" : 1,"Input-12" : 1,"Output-0" : 1, "Output-1" : 1,"Output-2" : 1, "Output-3" : 1 ,"Output-4" : 1,"Output-5" : 1,"Output-6" : 1,"Output-7" : 1,"Output-8" : 1,"Output-9" : 1,"Output-10" : 1,"Output-11" : 1,"Output-12" : 1}

	META_PREDICTOR_SCORE = {"r1" : 1,"r2" : 1,"r3" : 1, "R" : 1,"P" : 1,"S" : 1,"EneMostPlayed" : 1, "EneLeastPlayed" : 1,  "MyMostPlayed" : 1, "MyLeastPlayed" : 1 , "Input-0" : 1, "Input-1" : 1,"Input-2" : 1, "Input-3" : 1 ,"Input-4" : 1,"Input-5" : 1,"Input-6" : 1,"Input-7" : 1,"Input-8" : 1,"Input-9" : 1,"Input-10" : 1,"Input-11" : 1,"Input-12" : 1,"Output-0" : 1, "Output-1" : 1,"Output-2" : 1, "Output-3" : 1 ,"Output-4" : 1,"Output-5" : 1,"Output-6" : 1,"Output-7" : 1,"Output-8" : 1,"Output-9" : 1,"Output-10" : 1,"Output-11" : 1,"Output-12" : 1}
	 
	opt = random.choice(RPS)
	HISTORY = ["",""] # Enemy is 0, Player is 1
	for i in range(0,12):
		HISTORY[0] += random.choice(RPS)
		HISTORY[1] += random.choice(RPS)
	output = random.choice(RPS)
	next = {"R" : "P", "P" : "S", "S" :"R"}
	prev = {"R" : "S", "P" : "R", "S" :"P"}
	counter = 1
else:
	#Save HISTORY
	HISTORY[0]+= input
	HISTORY[1]+= output
	#Update Predictor Score	
	for i in STRATEGY:
		if PREDICTORS[i] == input:
			PREDICTOR_SCORE[i]+=2
			if opt1 == input :
				PREDICTOR_SCORE[i]+=7
			elif opt2 == input:
				PREDICTOR_SCORE[i]-=7
		else:
			PREDICTOR_SCORE[i]-=1
	# need be better than
	PREDICTORS["R"] = "R"
	PREDICTORS["P"] = "P"
	PREDICTORS["S"] = "S"
	PREDICTORS["r1"] = random.choice(RPS)
	PREDICTORS["r2"] = random.choice(RPS)
	PREDICTORS["r3"] = random.choice(RPS)
		
	# Predictor is Enemy's most played Move
	count = 0
	for i in RPS:
		tmp = HISTORY[0].count(i)
		if  tmp >count:
			count = tmp
			PREDICTORS["EneMostPlayed"] = i
	#Predictor is Enemy's least played Move
	count = 1337
	for i in RPS:
		tmp = HISTORY[0].count(i)
		if  tmp < count:
			count = tmp
			PREDICTORS["EneLeastPlayed"] = i
	# Predictor is My most played Move
	count = 0
	for i in RPS:
		tmp = HISTORY[1].count(i)
		if  tmp >count:
			count = tmp
			PREDICTORS["MyMostPlayed"] = i
	# Predictor is My least played Move
	count = 1337
	for i in RPS:
		tmp = HISTORY[1].count(i)
		if  tmp < count:
			count = tmp
			PREDICTORS["MyLeastPlayed"] = i
	# F-Predictorrs are Enemy's most recent Moves
	PREDICTORS["Input-0"] = input
	PREDICTORS["Input-1"] = HISTORY[0][-1]
	PREDICTORS["Input-2"] = HISTORY[0][-2]
	PREDICTORS["Input-3"] = HISTORY[0][-3]
	PREDICTORS["Input-4"] = HISTORY[0][-4]
	PREDICTORS["Input-5"] = HISTORY[0][-5]
	PREDICTORS["Input-6"] = HISTORY[0][-6]
	PREDICTORS["Input-7"] = HISTORY[0][-7]
	PREDICTORS["Input-8"] = HISTORY[0][-8]
	PREDICTORS["Input-9"] = HISTORY[0][-9]
	PREDICTORS["Input-10"] = HISTORY[0][-10]
	PREDICTORS["Input-11"] = HISTORY[0][-11]
	PREDICTORS["Input-12"] = HISTORY[0][-12]

	#Predictors are my most recent Moves
	PREDICTORS["Output-0"] = output
	PREDICTORS["Output-1"] = HISTORY[1][-1]
	PREDICTORS["Output-2"] = HISTORY[1][-2]
	PREDICTORS["Output-3"] = HISTORY[1][-3]
	PREDICTORS["Output-4"] = HISTORY[1][-4]
	PREDICTORS["Output-5"] = HISTORY[1][-5]
	PREDICTORS["Output-6"] = HISTORY[1][-6]
	PREDICTORS["Output-7"] = HISTORY[1][-7]
	PREDICTORS["Output-8"] = HISTORY[1][-8]
	PREDICTORS["Output-9"] = HISTORY[1][-9]
	PREDICTORS["Output-10"] = HISTORY[1][-10]
	PREDICTORS["Output-11"] = HISTORY[1][-11]
	PREDICTORS["Output-12"] = HISTORY[1][-12]



	#print(PREDICTOR_SCORE)
	maxP = max(PREDICTOR_SCORE.iteritems(), key=operator.itemgetter(1))[0]
	minP = min(PREDICTOR_SCORE.iteritems(), key=operator.itemgetter(1))[0]
	META_PREDICTOR_SCORE[maxP]+=1
	META_PREDICTOR_SCORE[minP]-=1
	#print(META_PREDICTOR_SCORE)
	opt1 = next[PREDICTORS[max(PREDICTOR_SCORE.iteritems(), key=operator.itemgetter(1))[0]]]
	opt2 = prev[PREDICTORS[min(PREDICTOR_SCORE.iteritems(), key=operator.itemgetter(1))[0]]]

	output = random.choice(opt1+opt2)

	counter += 1