import random
if input=='':
    numR = 0
    numP = 0
    numS = 0
elif input == 'R':
    numR += 1
elif input == 'P':
    numP += 1
elif input == 'S':
    numS += 1

Rscore = 100 + numS - numP
Pscore = 100 + numR - numS
Sscore = 100 + numP - numR

if Rscore == 0 and Pscore == 0 and Sscore == 0:
    output = random.choice(['R','P','S'])
else:
    if Rscore < 0:
        Rscore = 0
    if Pscore < 0:
        Pscore = 0
    if Sscore < 0:
        Sscore = 0
    scoresum = Rscore+Pscore+Sscore
    Rprob = Rscore*1.0/scoresum
    Pprob = Pscore*1.0/scoresum
    Sprob = Sscore*1.0/scoresum
    x = random.random()
    if x < Rprob:
        output = 'R'
    elif x < Rprob+Pprob:
        output = 'P'
    else:
        output = 'S'