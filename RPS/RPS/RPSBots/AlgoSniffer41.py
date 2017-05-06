import random
import math
#hopefully fixes a stupid bug in Algo Sniffer 3.2, 3.1 and 3
#guesses the algorithm that the opponent is using
#should always beat play last input, beat last input, always play rock, and skynet2, and spaghetti monkey
if not input:
	nummoves = 0
	urmoves = ['R','P','S']
	mode = 0
	lastoutput = 0
	prob = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	olast = 0
	ilast = 0
	monkeyness=0
	lastmonkeyoutput=0
else:
	ilast = {'R':0, 'P':1, 'S':2}[lastoutput]
	ind = 6*oprev + 2*iprev
	prob[ind] *= 0.95
	prob[ind+1] *= 0.95
	if ilast < 2:
		prob[ind+ilast] += 0.05
ind = 6*olast + 2*ilast
rateR = math.exp(5*(1-prob[ind]-2*prob[ind+1]))
rateP = math.exp(5*(2*prob[ind]+prob[ind+1]-1))
rateS = math.exp(5*(prob[ind+1]-prob[ind]))
randNum = random.random()*(rateR+rateP+rateS)

if randNum < rateR:
    monkeyoutput = "R"
elif randNum < rateR+rateP:
    monkeyoutput = "P"
else:
    monkeyoutput = "S"
oprev = olast
iprev = ilast
olast = {'R':0, 'P':1, 'S':2}[monkeyoutput]

if nummoves<3: #for the first 3 moves, play R, P, S.
	if nummoves==0:
		lastoutput = output = 'R'
	elif nummoves==1:
		lastoutput = output = 'P'
		urmoves[0]=input;
	elif nummoves==2:
		lastoutput = output = 'R'
		urmoves[1]=input;
else:
	if mode==0:
		urmoves[2] = input
		if urmoves == ['P','R','P']: #you are play last input
			mode=1
		elif urmoves == ['P','P','S'] or urmoves == ['R','P','S']: #you are beat last input
			mode=2
		elif urmoves == ['R','R','R']: #you are always play rock
			mode=3
		elif urmoves == ['S','S','R']: #you are skynet2
			mode=4
		else: #I don't know who you are but I'll always beat your last input
			mode=-1
			
	if mode==1:
		lastoutput = output = {'R':'P', 'P':'S', 'S':'R'}[lastoutput]
	elif mode==2:
		lastoutput = output = {'R':'S', 'P':'R', 'S':'P'}[lastoutput]
	elif mode==3:
		lastoutput = output = 'P'
	elif mode==4:
		lastoutput = output = {'R':'R', 'P':'P', 'S':'S'}[lastoutput]
	elif mode==5:
		lastoutput = output = {'R':'P', 'P':'S', 'S':'R'}[monkeyoutput]
	else:
		lastoutput = output = {'R':'P', 'P':'S', 'S':'R'}[input]
	if nummoves <50 and mode!=5: #attempt to sniff out the monkey in 50 moves
		if input == lastmonkeyoutput:
			monkeyness+=1;
		if monkeyness==40:
			mode = 5;
	
		
lastmonkeyoutput = monkeyoutput;
nummoves += 1