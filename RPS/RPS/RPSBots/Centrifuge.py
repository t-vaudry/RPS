import random
if not input:
	history1=""
	history2=""
	output = random.choice(['R','P','S'])
	movecombos = {'RP':'1','PS':'2','SR':'3','PR':'4','SP':'5','RS':'6','RR':'7','PP':'8','SS':'9'}
	predictorscore=[0,0,0]
	predictor=['R','R','R']
else:
	for i in range(3):
		predictorscore[i]*=0.87
		if input==predictor[i]:
			predictorscore[i]+=0.5
		elif input=={'R':'S', 'P':'R', 'S':'P'}[predictor[i]]:
			predictorscore[i]-=0.48
		else:
			predictorscore[i]-=0.02
	j=8
	history1+=input
	history2+=movecombos[input+output]
	length = len(history2)
	if j>length:
		j=length
	i = history2.rfind(history2[length-j:length-1],0,length-2)
	while i==-1:
		j-=1
		i = history2.rfind(history2[length-j:length-1],0,length-2)
		if j<2:
			break
	if i==-1 or j+i>=length:
		output = random.choice(['R','P','S'])
	else:
		predictor[0] = history1[j+i]
		predictor[1] = {'R':'P', 'P':'S', 'S':'R'}[history1[j+i]]
		predictor[2] = {'R':'P', 'P':'S', 'S':'R'}[predictor[1]]
		
	output = {'R':'P', 'P':'S', 'S':'R'}[predictor[predictorscore.index(max(predictorscore))]]
	output = {0:output,1:random.choice(['R','P','S'])}[ random.random() < 0.2 or max(predictorscore)<0]