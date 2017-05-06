#This is a DNA werfer. It werfs DNA!

import random
limit = 11

predictors=range(18)

for i in range(18):
	predictors[i]=random.choice(['R','P','S'])

if not input:
	beat={'R':'P','P':'S','S':'R'}
	urmoves=""
	mymoves=""
	DNAmoves=""
	output=random.choice(['R','P','S'])
	predictorscore=[1.2,0.7,0.7,0.6,0.6,0.6,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
	nuclease={'RP':'a','PS':'b','SR':'c','PR':'d','SP':'e','RS':'f','RR':'g','PP':'h','SS':'i'}
	length=0
else:
	for i in range(18):
		predictorscore[i]*=0.8
		predictorscore[i]+=(input==oldpredictors[i])/10.0
		predictorscore[i]-=(input=={'R':'S', 'P':'R', 'S':'P'}[oldpredictors[i]])/10.0
	
	#History matching
	urmoves+=input		
	mymoves+=output
	DNAmoves+=nuclease[input+output]
	length+=1
	
	j=limit
	if j>length:
		j=length
		
	while not DNAmoves[length-j:length] in DNAmoves[0:length-1]:
		j-=1
		if j<1:
			break
	if j>=1:
		i = DNAmoves.rfind(DNAmoves[length-j:length],0,length-1)
		predictors[0] = urmoves[j+i]
		predictors[1] = beat[mymoves[j+i]]
	j=limit
	if j>length:
		j=length
		
	while not urmoves[length-j:length] in urmoves[0:length-1]:
		j-=1
		if j<1:
			break
	if j>=1:
		i = urmoves.rfind(urmoves[length-j:length],0,length-1)
		predictors[2] = urmoves[j+i]
		predictors[3] = beat[mymoves[j+i]]
	j=limit
	if j>length:
		j=length
		
	while not mymoves[length-j:length] in mymoves[0:length-1]:
		j-=1
		if j<1:
			break
	if j>=1:
		i = mymoves.rfind(mymoves[length-j:length],0,length-1)
		predictors[4] = urmoves[j+i]
		predictors[5] = beat[mymoves[j+i]]
	
	for i in range(6,18):
		predictors[i]={'R':'S', 'P':'R', 'S':'P'}[predictors[i-6]]
		

	
	#compare predictors
	best=-100
	for i in range(18):
		if predictorscore[i]>best:
			output = predictors[i]
			best = predictorscore[i]
			
output = {'R':'P','P':'S','S':'R'}[output] #attempt to win	

oldpredictors=predictors