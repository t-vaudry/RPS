import random
#guesses the algorithm that the opponent is using
if input=="":
	nummoves = 0
	mymoves = urmoves = [0,0,0]
	mode = 0

if nummoves < 3:
	move = nummoves+1
	if move==1:
		output = 'R'
	elif move==2:
		output = 'P'
	else:
		output = 'S'
		
	mymoves[nummoves] = output	
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
		output = {'R':'P', 'P':'S', 'S':'R'}[lastoutput]
	elif mode==2:
		output = {'R':'S', 'P':'R', 'S':'P'}[lastoutput]
	elif mode==3:
		output = 'P'
	elif mode==4:
		output = {'R':'R', 'P':'P', 'S':'S'}[lastoutput]
	else:
		output = {'R':'P', 'P':'S', 'S':'R'}[input]
lastoutput = output