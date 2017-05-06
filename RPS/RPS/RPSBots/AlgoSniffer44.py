import random
#guesses the algorithm that the opponent is using
#should always beat: 
#play last input
#beat last input
#always play rock
#skynet2
#algo sniffer 3.2, 3.3, 3.4, 3.4v, 3.4vv, 4
if not input:
	nummoves = 0
	urmoves = ['R','P','S']
	mode = 0
	lastoutput = 0
	loserness = 0

if nummoves<3: #for the first 3 moves, play R, P, something
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
		lastoutput = output = random.choice(["R", "P", "S"])
	else:
		lastoutput = output = {'R':'P', 'P':'S', 'S':'R'}[input]
	if nummoves>10 and nummoves<110 and mode!=5: #if we are losing most of the time, just go random
		if input == {'R':'P', 'P':'S', 'S':'R'}[lastoutput]:
			loserness+=1;
		if loserness > 53:
			mode = 5;

nummoves += 1