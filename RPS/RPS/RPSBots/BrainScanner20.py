import math,random
#This program detects brain waves through your computer screen to determine how you think and what kind of #program you would write.
memory=2
if (input=='R' and output=='P') or (input=='P' and output=='S') or (input=='S' and output=='R'):
	print("Match won!")
	try:
		wcount+=1
		print(str(wcount)+ " wins")
		print(str(lcount)+ " losses")
	except NameError:
		wcount=0
else:
	print("Lost!")
	try:
		lcount+=1
		print(str(wcount)+ " wins")
		print(str(lcount)+ " losses")
	except NameError:
		lcount=0
try:
	count+=2
except NameError:
	count=0
try:
	hist+=input
except NameError:
	hist=""
	hist+=input
try:
	prev['ABCDE']=0
except NameError:
	prev=dict()
l=len(hist)
if l>=memory+2:
	word=str(hist[l-memory-2])
	for i in range(-memory-1,-2):
		word=word+str(hist[l+i])
	print("Adding "+word+" with branch "+str(hist[l-1]))
	if not word in prev:
		prev[word]=dict()
	if hist[l-1] in prev[word]:
		prev[word][hist[l-1]]+=1
	else:
		prev[word][hist[l-1]]=1
else:
	print("Adding "+input)
if count<100:
	output = random.choice(["R","P","S"])
else:
	guess=str(hist[l-memory])
	for i in range(-memory+1,0):
		guess=guess+str(hist[l+i])
	
	if guess in prev:
		predict=max(prev[guess], key = lambda x: prev[guess].get(x) )
		output={'R':'P', 'P':'S', 'S':'R'}[predict]
		print("Guessing "+guess+" will be "+output)
	else:
		print("Never seen this before! Choosing random...")
		output=random.choice(["R","P","S"])
hist+=output