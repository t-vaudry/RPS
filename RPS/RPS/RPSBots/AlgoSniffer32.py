import random
#hopefully fixes a stupid bug in Algo Sniffer 3.1 and 3
#guesses the algorithm that the opponent is using
if input=="":
	nummoves = 0
	urmoves = ['R','P','S']
	mode = 0
	lastoutput = 'S'

if nummoves < 3:
	if nummoves==0:
		lastoutput = output = 'R'
	elif nummoves==1:
		lastoutput = output = 'P'
	elif nummoves==2:
		lastoutput = output = 'S'
	urmoves[nummoves] = input
	nummoves += 1
else:
	if mode==0:
		if urmoves == ['P','R','P']: #you are play last input
			mode=1
		elif urmoves == ['P','P','S']: #you are beat last input
			mode=2
		elif urmoves == ['R','R','R']: #you are always play rock
			mode=3
		elif urmoves == ['S','S','R']: #you are skynet2
			mode=4
		else: #I don't know who you are but I'll always beat your last input
			mode=5
			
	if mode==1:
		lastoutput = output = {'R':'P', 'P':'S', 'S':'R'}[lastoutput]
	elif mode==2:
		lastoutput = output = {'R':'S', 'P':'R', 'S':'P'}[lastoutput]
	elif mode==3:
		lastoutput = output = 'P'
	elif mode==4:
		lastoutput = output = {'R':'R', 'P':'P', 'S':'S'}[lastoutput]
	else:
		lastoutput = output = {'R':'P', 'P':'S', 'S':'R'}[input]