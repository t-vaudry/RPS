import math,random
p=0.8
memory=8
if input=="":
	count=0
	wcount=0
	lcount=0
	prev=dict()
	hist=""
	abc=0
else:
	count+=1
	hist+=input
	n=1000-count
	if wcount-lcount>n-(math.sqrt(1+8*(1-p)*(n+1)*(n+1))-1)/2:
		abc=1
if (input=='R' and output=='P') or (input=='P' and output=='S') or (input=='S' and output=='R'):
	wcount+=1
else:
	lcount+=1
l=len(hist)
if l>=memory+2:
	word=str(hist[l-memory-2])
	for i in range(-memory-1,-2):
		word=word+str(hist[l+i])
	if not word in prev:
		prev[word]=dict()
	if hist[l-1] in prev[word]:
		prev[word][hist[l-1]]+=1
	else:
		prev[word][hist[l-1]]=1
if count<50:
	output = random.choice(["R","P","S"])
else:
	guess=str(hist[l-memory])
	for i in range(-memory+1,0):
		guess=guess+str(hist[l+i])
	if guess in prev:
		predict=max(prev[guess], key = lambda x: prev[guess].get(x) )
		output={'R':'P', 'P':'S', 'S':'R'}[predict]
	else:
		output=random.choice(["R","P","S"])
if abc==1:
		output=random.choice(["R","P","S"])
hist+=output