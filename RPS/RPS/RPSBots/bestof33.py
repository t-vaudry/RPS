import math
import random

lastmatch=0

r = random.randrange(0,100)
if not input:
	lloutput = 'P'
	loutput = output = 'P'
	num = 0;
	prob = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        olast = 0
        ilast = 0
        urmoves=""
	mymoves=""
	output = random.choice(['R','P','S'])
	candidate = ['P','P','P','P','P','P','P']
	score = [0,0,0,0,0,0,0]

else:
	mymoves += input
	for i in range(0, 6):
		score[i] *= 0.95
		score[i] += (4 + {'R':0,'P':1,'S':2}[candidate[i]] - {'R':0,'P':1,'S':2}[input])%3 - 1
	if num<3:
		output = 'P'
		num+=1;
	elif input == {'R':'P','P':'S','S':'R'}[lloutput]:
		output = {'R':'S','P':'R','S':'P'}[loutput]
	elif input == {'R':'S','P':'R','S':'P'}[lloutput]:
		output = {'R':'R','P':'P','S':'S'}[loutput]
	elif input == {'R':'R','P':'P','S':'S'}[lloutput]:
		output = {'R':'P','P':'S','S':'R'}[loutput]
	ilast = {'R':0, 'P':1, 'S':2}[input]
        ind = 6*oprev + 2*iprev
        prob[ind] *= 0.95
        prob[ind+1] *= 0.95
        if ilast < 2:
            prob[ind+ilast] += 0.05
        urmoves+=input
        
lloutput = loutput
loutput = output

ind = 6*olast + 2*ilast
rateR = math.exp(5*(1-prob[ind]-2*prob[ind+1]))
rateP = math.exp(5*(2*prob[ind]+prob[ind+1]-1))
rateS = math.exp(5*(prob[ind+1]-prob[ind]))
randNum = random.random()*(rateR+rateP+rateS)

if randNum < rateR and r<20:
    output = "R"
elif randNum < rateR+rateP and r<20:
    output = "P"
elif r<20:
    output = "S"
elif r>=20 and r<50:
	output = random.choice(['R','P','S'])
	for i in range(len(urmoves)-1,20,-1):
		match=0
		j=1
		while mymoves[i-j]==mymoves[len(urmoves)-j]:
			match+=1
			if match>lastmatch:
				lastmatch=match
				output=urmoves[i]
			if match>20:
				break
			j+=1
	
	output =  {'R':'P', 'P':'S', 'S':'R'}[output]
elif r>=50 and r<65:
	candidate[0] = random.choice(['R','P','S'])
	candidate[1] = random.choice(['R','P','S'])
	candidate[4] = random.choice(['R','P','S'])
	index = 0
	limit = 45
	longestMatch = 0
	
	while index < len(mymoves)-2:
		index2 = index
		index3 = len(mymoves)-2
		length = 0
		while index2 >= 0:
			if mymoves[index2] != mymoves[index3] or mymoves[index2+1] != mymoves[index3+1]:
				break
			index2 -= 2
			index3 -= 2
			length += 1
			if length > limit:
				break
		if length > longestMatch:
			longestMatch = length
			candidate[1] = mymoves[index+3]
			candidate[4] = mymoves[index+2]
		if length > limit:
			break
		index += 2
	
	for i in [2,3,5,6]:
		candidate[i] = {'R':'S','P':'R','S':'P'}[candidate[i-1]]
	
	best = 0
	output = candidate[0]
	for i in range(1, 6):
		if (score[i] > score[best]):
			best = i
			output = candidate[i]

mymoves+=output

oprev = olast
iprev = ilast
olast = {'R':0, 'P':1, 'S':2}[output]