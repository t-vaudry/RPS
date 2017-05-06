import math,random

input='R'

try:
	prev['aaaaaa']=0
except NameError:
	prev=dict()

try:
	hist+=input
except NameError:
	hist=""
	hist+=input

print("Length: %.f" % len(hist))

if len(hist)<6:
	output = random.choice(["R","P","S"])
	

elif len(hist)<50:
	output = random.choice(["R","P","S"])
	l=len(hist)
	word=''.join([hist[l-6],hist[l-5],hist[l-4],hist[l-3],hist[l-2],hist[l-1]])
	if word in prev:
		prev[word]+=1
	else:
		prev[word]=1
	
else:
	if len(hist)==202:
		hist.remove(hist[0])
		hist.remove(hist[0])
	l=len(hist)
	word=''.join([hist[l-6],hist[l-5],hist[l-4],hist[l-3],hist[l-2],hist[l-1]])
	if word in prev:
		prev[word]+=1
	else:
		prev[word]=1

	for guess in prev:
		print(guess)



hist+=output