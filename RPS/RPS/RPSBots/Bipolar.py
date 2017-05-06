import math,random
memory=8
if (input=='R' and output=='P') or (input=='P' and output=='S') or (input=='S' and output=='R'):
	try:
		wcount+=1
	except NameError:
		wcount=0
else:
	try:
		lcount+=1
	except NameError:
		lcount=0
try:
	count+=2
except NameError:
	count=0
	strike=0
try:
	hist+=input
except NameError:
	hist=""
	hist+=input
try:
	prev['ABCDE']=0
	prev2['ABCDE']=0
except NameError:
	prev=dict()
	prev2=dict()
l=len(hist)
if l>=memory+2:
	word=str(hist[l-memory-2])
	for i in range(-memory-1,-2):
		word=word+str(hist[l+i])
	if not word in prev:
		prev[word]=dict()
		prev2[word]=dict()
	if hist[l-1] in prev[word]:
		prev[word][hist[l-1]]+=1
	else:
		prev[word][hist[l-1]]=1
	if hist[l-2] in prev2[word]:
		prev2[word][hist[l-2]]+=1
	else:
		prev2[word][hist[l-2]]=1
if count<100:
	output=random.choice(["R","P","S"])
else:
	guess=str(hist[l-memory])
	for i in range(-memory+1,0):
		guess=guess+str(hist[l+i])
	if guess in prev:
		predict=max(prev[guess], key = lambda x: prev[guess].get(x) )
		output={'R':'P', 'P':'S', 'S':'R'}[predict]
		predict2=max(prev2[guess], key = lambda x: prev2[guess].get(x) )
		if output==predict2 and lcount>wcount:
			strike=strike+1
			if strike>200:
				output={'R':'S', 'P':'R', 'S':'P'}[output]
	else:
		output=random.choice(["R","P","S"])
hist+=output