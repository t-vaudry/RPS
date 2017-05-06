import math,random
aaa=30
if (input=='R' and output=='P') or (input=='P' and output=='S') or (input=='S' and output=='R'):
	print("Match won!")
	try:
		wcount+=1
	except NameError:
		wcount=0
else:
	print("Lost!")
	try:
		lcount+=1
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
if l>=8:
	word=''.join([hist[l-8],hist[l-7],hist[l-6],hist[l-5],hist[l-4],hist[l-3]])
	if not word in prev:
		prev[word]=dict()
	if hist[l-1] in prev[word]:
		prev[word][hist[l-1]]+=1
	else:
		prev[word][hist[l-1]]=0
if count<50:
	output = random.choice(["R","P","S"])
else:
	guess=''.join([hist[l-6],hist[l-5],hist[l-4],hist[l-3],hist[l-2],hist[l-1]])
	if guess in prev:
		predict=max(prev[guess])
		output={'R':'P', 'P':'S', 'S':'R'}[predict]
	else:
		output=random.choice(["R","P","S"])
hist+=output
try:
	if (wcount>lcount+aaa):
		output=random.choice(["R","P","S"])
except NameError:
	output=random.choice(["R","P","S"])