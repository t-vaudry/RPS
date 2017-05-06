import math
import random

r = random.randrange(0,100)
if not input:
	lloutput = 'P'
	loutput = output = 'P'
	num = 0;
	prob = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        olast = 0
        ilast = 0
else:
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
lloutput = loutput
loutput = output

ind = 6*olast + 2*ilast
rateR = math.exp(5*(1-prob[ind]-2*prob[ind+1]))
rateP = math.exp(5*(2*prob[ind]+prob[ind+1]-1))
rateS = math.exp(5*(prob[ind+1]-prob[ind]))
randNum = random.random()*(rateR+rateP+rateS)

if randNum < rateR and r<50:
    output = "R"
elif randNum < rateR+rateP and r<50:
    output = "P"
elif r<50:
    output = "S"
elif r>=50 and r<60:
	move = random.randrange(0,3)
	if move == 1:
		output = "R"
	elif move == 2:
		output = "P"
	else:
		output = "S"

oprev = olast
iprev = ilast
olast = {'R':0, 'P':1, 'S':2}[output]