import random, operator
SIZE = 12

if input == "":
	STRATEGY_SCORES 		= 	[[1,1,1],[1,1,1],[1,1,1]]
	STRATEGY 				= 	[['RR', 'RR', 'RR'], ['RR', 'RR', 'RR'], ['RR', 'RR', 'RR']]
	STRATEGY_SELECTOR		=	8
	STRATEGY_SELECTOR_SCORE = 	[1,1,1,1,1,1,1,1,1]
	HISTORY					= 	[""]*2
	LEVEL 					= 	[[0,0,0],[0,0,0]]
	BANGBOOM 				= [(1, 'PP'), (1, 'PS'), (1, 'RP'), (1, 'SP'), (1, 'SR'), (1, 'SS'), (1, 'PR'), (1, 'RR'), (1, 'RS')]
	NOPE = True
	bx		= 	{"R" : "P", "P" : "S", "S" : "R"}
	bxy 	= 	{'PP': 'S', 'SS': 'R', 'RR':'P', 'PS': 'S', 'PR': 'P', 'RS': 'R', 'RP': 'P', 'SP': 'S', 'SR': 'R'}
	output 	= 	random.choice(["R","P","S"])
else:
	#print(input)	
	HISTORY[0] += input
	HISTORY[1] += output
	LEVEL = [[0,0,0],[0,0,0]]
	for i in range(0,3):
		for j in range(0,3):
			if bx[input] == bx[STRATEGY[i][j][0]] or bx[STRATEGY[i][j][0]] == output:
				STRATEGY_SCORES[i][j]+=1
	for i in range(0,9):
		if bx[input] == bx[BANGBOOM[i][1][0]]:
			STRATEGY_SELECTOR_SCORE[i]+= 1
	for i in range(1,1+SIZE):
		for j in range(0,2):
			LEVEL[j][0] +=HISTORY[j].count((HISTORY[j]+"R")[-i:])
			LEVEL[j][1] +=HISTORY[j].count((HISTORY[j]+"P")[-i:])
			LEVEL[j][2] +=HISTORY[j].count((HISTORY[j]+"S")[-i:])
	MOVES = [zip(LEVEL[0],["R","P","S"]),zip(LEVEL[1],["R","P","S"])]
	MOVES[0].sort()	
	MOVES[1].sort()
	for i in range(0,3):
		for j in range(0,3):
			STRATEGY[i][j] = MOVES[0][i][1]+MOVES[1][j][1]	
	BANGBOOM = zip(STRATEGY_SCORES[0],STRATEGY[0])+zip(STRATEGY_SCORES[1],STRATEGY[1])+zip(STRATEGY_SCORES[2],STRATEGY[2])
	BANGBOOM.sort()
	DERP = []*9
	for i in range(0,9):
		DERP+= [(STRATEGY_SELECTOR_SCORE[i]*BANGBOOM[i][0]/64,BANGBOOM[i][1])]
	DERP.sort()
	#print(DERP)
	if NOPE :
		output = random.choice(["R","P","S"])
		NOPE = False
	else:
		output = bxy[random.choice(DERP[6:])[1]]
		NOPE = True