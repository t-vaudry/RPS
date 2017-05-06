import random
if not input:
	moves = ['R','P','S']
	urmoves=[0,0,0]
	lastoutput=output = 'S'
	mymoves=[0,0,0]
else:
	urmoves[0] = urmoves[1]
	urmoves[1] = urmoves[2]
	urmoves[2] = {'R':0,'P':1,'S':2}[input]
	if urmoves==mymoves:
		output = moves[(mymoves[2]+1)%3]
	elif urmoves[0]==(mymoves[0]+1)%3 and urmoves[1]==(mymoves[1]+1)%3 and urmoves[2]==(mymoves[2]+1)%3:
		output = moves[(mymoves[2]+2)%3]
	elif urmoves[0]==(mymoves[0]+2)%3 and urmoves[1]==(mymoves[1]+2)%3 and urmoves[2]==(mymoves[2]+2)%3:
		output = moves[(mymoves[2]+3)%3]
	else:
		output = random.choice(['R', 'P', 'S'])
	mymoves[0] = mymoves[1]
	mymoves[1] = mymoves[2]
	mymoves[2] = {'R':0,'P':1,'S':2}[lastoutput]
	lastoutput = output