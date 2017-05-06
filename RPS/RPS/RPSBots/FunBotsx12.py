import math,random
memory=8
strike=3
if input=="":
	wcount=0
	lcount=0
	count=0
	hist=""
	prev=dict()
	prev2=dict()
	guess=""
else:
	hist+=input
	count+=2
l=len(hist)
if (input=='R' and output=='P') or (input=='P' and output=='S') or (input=='S' and output=='R'):
	wcount+=1
elif (input=='P' and output=='R') or (input=='S' and output=='P') or (input=='R' and output=='S'):
	lcount+=1
	if count>=memory+2:
		if guess in prev2 and predict in prev2[guess]:
			prev2[guess][predict]-=1
if count>=memory+2:
	word=str(hist[l-memory-2])
	for i in range(-memory-1,-2):
		word=word+str(hist[l+i])
	if not word in prev:
		prev[word]=dict()
		prev2[word]=dict()
	if hist[count-1] in prev[word]:
		prev[word][hist[l-1]]+=1
	else:
		prev[word][hist[l-1]]=1
		prev2[word][hist[l-1]]=strike
if count<8 or wcount>60+lcount:
	output=random.choice(["R","P","S"])
else:
	guess=str(hist[count-memory])
	for i in range(-memory+1,0):
		guess=guess+str(hist[count+i])
	if guess in prev:
		predict=max(prev[guess], key = lambda x: prev[guess].get(x) )
		if prev2[guess][predict]>0:
			output={'R':'P', 'P':'S', 'S':'R'}[predict]
		else:
			output=predict
	else:
		output=random.choice(["R","P","S"])
hist+=output