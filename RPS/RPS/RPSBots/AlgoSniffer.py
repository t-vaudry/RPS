import random

if input=="":
	nummoves = 0
	mymoves = urmoves = [0,0,0]
	mode = 0

if nummoves < 3:
	move = random.randrange(0,3)
	if move==1:
		output = "R"
	elif move==2:
		output = "P"
	else:
		output = "S"
		
	mymoves[nummoves] = move	
	if input=="R":
		urmoves[nummoves] = 1
	elif input=="P":
		urmoves[nummoves] = 2
	else:
		urmoves[nummoves] = 3
	
	nummoves += 1
else:
	if mode==0:
		if urmoves[1]==mymoves[0] and urmoves[2]==mymoves[1]:
			mode=1
		elif urmoves[1]==mymoves[0]%3+1 and urmoves[2]==mymoves[1]%3+1:
			mode=2
		elif urmoves[0]==1 and urmoves[1]==1 and urmoves[2]==1:
			mode=3
		else:
			mode=4
	if mode==1:
		output = {'R':'P', 'P':'S', 'S':'R'}[output]
	elif mode==2:
		output = {'R':'S', 'P':'R', 'S':'P'}[output]
	elif mode==3:
		output = 'P'
	else:
		output = {'R':'P', 'P':'S', 'S':'R'}[input]