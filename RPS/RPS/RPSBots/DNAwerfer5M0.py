#This is a DNA werfer. It werfs DNA!

import random

number_of_predictors = 36 #yes, this really has 36 predictors.

predictors=range(number_of_predictors)

for i in range(number_of_predictors):
	predictors[i]=random.choice(['R','P','S'])

if not input:
	beat={'R':'P','P':'S','S':'R'}
	urmoves=""
	mymoves=""
	DNAmoves=""
	output=random.choice(['R','P','S'])
	predictorscore=range(number_of_predictors)
	nuclease={'RP':'a','PS':'b','SR':'c','PR':'d','SP':'e','RS':'f','RR':'g','PP':'h','SS':'i'}
	length=0
else:
	for i in range(number_of_predictors):
		predictorscore[i]+=(input==oldpredictors[i])*3
		if input==beat[beat[oldpredictors[i]]]:
			predictorscore[i]=0
	
	#History matching
	urmoves+=input		
	mymoves+=output
	DNAmoves+=nuclease[input+output]
	length+=1
	
	limit = min([length,10])
	j=limit
	while j>=1 and not DNAmoves[length-j:length] in DNAmoves[0:length-1]:
		j-=1
	if j>=1:
		i = DNAmoves.find(DNAmoves[length-j:length],0,length-1) 
		predictors[0] = urmoves[j+i] 
		predictors[1] = beat[mymoves[j+i]] 
		i = DNAmoves.rfind(DNAmoves[length-j:length],0,length-1) 
		predictors[2] = urmoves[j+i] 
		predictors[3] = beat[mymoves[j+i]]
	j=limit			
	while j>=1 and not urmoves[length-j:length] in urmoves[0:length-1]:
		j-=1
	if j>=1:
		i = urmoves.find(urmoves[length-j:length],0,length-1) 
		predictors[4] = urmoves[j+i] 
		predictors[5] = beat[mymoves[j+i]] 
		i = urmoves.rfind(urmoves[length-j:length],0,length-1) 
		predictors[6] = urmoves[j+i] 
		predictors[7] = beat[mymoves[j+i]] 
	j=limit
	while j>=1 and not mymoves[length-j:length] in mymoves[0:length-1]:
		j-=1
	if j>=1:
		i = mymoves.find(mymoves[length-j:length],0,length-1) 
		predictors[8] = urmoves[j+i] 
		predictors[9] = beat[mymoves[j+i]]
		i = mymoves.rfind(mymoves[length-j:length],0,length-1) 
		predictors[10] = urmoves[j+i] 
		predictors[11] = beat[mymoves[j+i]]
	
	for i in range(12,36):
		predictors[i]=beat[beat[predictors[i-12]]] #Trying to second guess me?
	
	#compare predictors
	output = beat[predictors[predictorscore.index(max(predictorscore))]]

oldpredictors=predictors