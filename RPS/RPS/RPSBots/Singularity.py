import random
if input == "":
	R = {'R':0,'P':0,'S':0}
	P = {'R':0,'P':0,'S':0}
	S = {'R':0,'P':0,'S':0}
	bout=1
	lastPlay = 'P'
else:
	if winner(input, lastPlay):
		incrementWinTable(input, lastPlay)
	if bout<25:
		lastPlay = random.choice(['R','P','S'])
		bout+=1
	elif input == "R":
		lastPlay = max(R, key=lambda x: R[x[0]])
	elif input == "P":
		lastPlay = max(P, key=lambda x: P[x[0]])
	elif input == "S":
		lastPlay = max(S, key=lambda x: S[x[0]])
output = lastPlay


def winner(competitorPlay, myPlay):
	if competitorPlay == 'R':
		return myPlay == 'P'
	elif competitorPlay == 'P':
		return myPlay == 'S'
	else:
		return myPlay == 'R'
	
def incrementWinTable(competitorPlay, myPlay):
	if competitorPlay == 'R':
		R[myPlay]+= 1
	elif competitorPlay == 'P':
		P[myPlay]+= 1
	else:
		S[myPlay]+= 1