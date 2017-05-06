import random

r = random.randrange(0,2)
if r==0 or r==1:

	if not input:
		nummoves = 0
		urmoves = ['R','P','S']
		mode = 0
		lastoutput = 0

	if nummoves<3: #for the first 3 moves, play R, P, S.
		if nummoves==0:
			lastoutput = output = 'R'
		elif nummoves==1:
			lastoutput = output = 'P'
			urmoves[0]=input;
		elif nummoves==2:
			lastoutput = output = 'S'
			urmoves[1]=input;
		nummoves += 1
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
				mode=5
			#print "urmoves:"
			#print urmoves
			#print "mode:"
			#print mode
			
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
else:
	move = random.randrange(0,3)
	if move == 1:
		output = "R"
	elif move == 2:
		output = "P"
	else:
		output = "S"