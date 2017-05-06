import math
import random

lastmatch=0

r = random.randrange(0,100)

if not input:
    hist = [[[[1/3,1/3],[1/3,1/3],[1/3,1/3],[1/3,1/3],[1/3,1/3],[1/3,1/3],[1/3,1/3],[1/3,1/3],[1/3,1/3]] for i in range(9)] for j in range(9)]
    a_hist = [[[[1/3,1/3],[1/3,1/3],[1/3,1/3],[1/3,1/3],[1/3,1/3],[1/3,1/3],[1/3,1/3],[1/3,1/3],[1/3,1/3]] for i in range(9)] for j in range(9)]
    prev = [0,0,0]
    olast = 0
    ilast = 0
    candidate = [1,0,1,2,0,1,2]
    score = [1,2,0,0,0,0,2]
    weight = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    urmoves=""
    mymoves=""
    output = random.choice(['R','P','S'])
    matchHistory = ""
else:
    ilast = {'R':0, 'P':1, 'S':2}[input]
    for i in range(7):
        score[i] *= 0.96
        for j in range(3):
            score[i] += ((4 + j - ilast) % 3 - 1)*weight[i][j]
    
    hist[prev[2]][prev[0]][prev[1]][0] *= 0.75
    hist[prev[2]][prev[0]][prev[1]][1] *= 0.75
    a_hist[prev[2]][prev[0]][prev[1]][0] *= 0.75
    a_hist[prev[2]][prev[0]][prev[1]][1] *= 0.75
    if ilast < 2:
        hist[prev[2]][prev[0]][prev[1]][ilast] += 0.25
    if olast < 2:
        a_hist[prev[2]][prev[0]][prev[1]][olast] += 0.25
    for i in range(0,8):
        hist[prev[2]][i][prev[1]][0] *= 0.9
        hist[prev[2]][i][prev[1]][1] *= 0.9
        a_hist[prev[2]][i][prev[1]][0] *= 0.9
        a_hist[prev[2]][i][prev[1]][1] *= 0.9
        if ilast < 2:
            hist[prev[2]][i][prev[1]][ilast] += 0.1
        if olast < 2:
            a_hist[prev[2]][i][prev[1]][olast] += 0.1
        for j in range(0,8):
            hist[prev[2]][i][j][0] *= 0.96
            hist[prev[2]][i][j][1] *= 0.96
            a_hist[prev[2]][i][j][0] *= 0.96
            a_hist[prev[2]][i][j][1] *= 0.96
            if ilast < 2:
                hist[prev[2]][i][j][ilast] += 0.04
            if olast < 2:
                a_hist[prev[2]][i][j][olast] += 0.04
    prev[0] = prev[1]
    prev[1] = prev[2]
    prev[2] = 3*olast + ilast
    urmoves += input

prob = hist[prev[2]][prev[0]][prev[1]]
rateR = math.exp(5*(1-prob[0]-2*prob[1]))
rateP = math.exp(5*(2*prob[0]+prob[1]-1))
rateS = math.exp(5*(prob[1]-prob[0]))
randNum = random.random()*(rateR+rateP+rateS)
if randNum < rateR:
    candidate[1] = 0
elif randNum < rateR+rateP:
    candidate[1] = 1
else:
    candidate[1] = 2
weight[1][0] = rateR/(rateR+rateP+rateS)
weight[1][1] = rateP/(rateR+rateP+rateS)
weight[1][2] = rateS/(rateR+rateP+rateS)

prob = a_hist[prev[2]][prev[0]][prev[1]]
rateR = math.exp(5*(1-prob[0]-2*prob[1]))
rateP = math.exp(5*(2*prob[0]+prob[1]-1))
rateS = math.exp(5*(prob[1]-prob[0]))
randNum = random.random()*(rateR+rateP+rateS)
if randNum < rateR:
    candidate[4] = 0
elif randNum < rateR+rateP:
    candidate[4] = 1
else:
    candidate[4] = 2
weight[4][0] = rateR/(rateR+rateP+rateS)
weight[4][1] = rateP/(rateR+rateP+rateS)
weight[4][2] = rateS/(rateR+rateP+rateS)

candidate[0] = random.choice(['R','P','S'])
weight[0][0] = weight[0][1] = weight[0][2] = 0
for i in [2,3,5,6]:
    candidate[i] = (candidate[i-1] + 1) % 3
    weight[i][0] = weight[i-1][2]
    weight[i][1] = weight[i-1][0]
    weight[i][2] = weight[i-1][1]

best = score[0]
olast = candidate[0]
for i in range(1, 7):
    if (best < score[i]):
        best = score[i]
        olast = candidate[i]
output = {0:'R', 1:'P', 2:'S'}[olast]


if r<15:
	for i in range(len(urmoves)-1,20,-1):
		match=0
		j=1
		while mymoves[i-j]==mymoves[len(urmoves)-j]:
			match+=1
			if match>lastmatch:
				lastmatch=match
				output=urmoves[i]
			if match>15:
				break
			j+=1
	
	output =  {'R':'P', 'P':'S', 'S':'R'}[output]

mymoves += output