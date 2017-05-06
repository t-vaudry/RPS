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
	word=[]
	for i in range(-memory-2,-2):
		word.append(str(hist[l+i]))
	t1=word[0]
	t2=t1
	t3=t1
	for a in range(len(word)):
		if word[a]==t1:
			word[a]='A'
		elif word[a]==t2:
			word[a]='B'
		elif word[a]==t3:
			word[a]='C'
		elif t2==t1:
			t2=word[a]
			word[a]='B'
		else:
			word[a]='C'
	word=''.join(word)
	let=str(hist[l-1])
	if let==t1:
		let='A'
	elif let==t2:
		let='B'
	else:
		let='C'
	if not word in prev:
		prev[word]=dict()
	if let in prev[word]:
		prev[word][let]+=1
	else:
		prev[word][let]=1
if count<100:
	output = random.choice(["R","P","S"])
else:
	guess=[]
	for i in range(-memory,0):
		guess.append(str(hist[l+i]))
	t1=guess[0]
	t2=t1
	t3=t1
	for a in range(len(guess)):
		if guess[a]==t1:
			guess[a]='A'
		elif guess[a]==t2:
			guess[a]='B'
		elif guess[a]==t3:
			guess[a]='C'
		elif t2==t1:
			t2=guess[a]
			guess[a]='B'
		else:
			guess[a]='C'
	guess=''.join(guess)
	if guess in prev:
		abc=prev[guess]
		predict=max(prev[guess], key = lambda x: prev[guess].get(x) )
		if predict=='A':
			predict=t1
		elif predict=='B':
			predict=t2
		else:
			predict=t3
		output={'R':'P', 'P':'S', 'S':'R'}[predict]
	else:
		output=random.choice(["R","P","S"])
hist+=output