# author: blue-tomato
#
# frequency analyzer with dynamic depth

import random

if input == '':
    num = {}
    lastinput = ''
    maxdepth = 5
    randthresh = 4.0
    depthscore = [0.0,0.0,0.0,0.0,0.0]
    depthlastout = ['','','','','']
else:
    for i in range(0,maxdepth):
        if input == 'R':
            if depthlastout[i] == 'P':
                depthscore[i] += 1.0
            if depthlastout[i] == 'S':
                depthscore[i] -= 1.0
        if input == 'P':
            if depthlastout[i] == 'S':
                depthscore[i] += 1.0
            if depthlastout[i] == 'R':
                depthscore[i] -= 1.0
        if input == 'S':
            if depthlastout[i] == 'R':
                depthscore[i] += 1.0
            if depthlastout[i] == 'P':
                depthscore[i] -= 1.0
        depthscore[i] *= 0.97

for i in range(0,len(lastinput)+1):

    manyin = input
    if i > 0:
        manyin = lastinput[-i] + input
    if manyin in num:
        num[manyin] += 1
    else:
        num[manyin] = 1
        
        
    numR = 0
    numP = 0
    numS = 0
    
    x = manyin[1:]+'R'
    if x in num:
        numR = num[x]
    x = manyin[1:]+'P'
    if x in num:
        numP = num[x]
    x = manyin[1:]+'S'
    if x in num:
        numS = num[x]

    if numR + numP + numS <= 2:
        depthlastout[i] = ''
    elif numR > numP and numR > numS:
        depthlastout[i] = 'P'
    elif numP > numR and numP > numS:
        depthlastout[i] = 'S'
    elif numS > numR and numS > numP:
        depthlastout[i] = 'R'
    else:
        depthlastout[i] = ''
        
Rscore = 0
Pscore = 0
Sscore = 0
if max(depthscore) > randthresh:
    for i in range(0,maxdepth):
        if depthscore[i] > 0:
            if depthlastout[i] == 'R':
                Rscore += depthscore[i]
            if depthlastout[i] == 'P':
                Pscore += depthscore[i]
            if depthlastout[i] == 'S':
                Sscore += depthscore[i]

if Rscore > Pscore and Rscore > Sscore:
    output = 'R'
elif Pscore > Rscore and Pscore > Sscore:
    output = 'P'
elif Sscore > Rscore and Sscore > Pscore:
    output = 'S'
elif Rscore == Pscore and Pscore == Sscore:
    output = random.choice(['R','P','S'])
elif Rscore == Pscore:
    output = random.choice(['R','P'])
elif Rscore == Sscore:
    output = random.choice(['R','S'])
else:
    output = random.choice(['P','S'])
    
    

if len(lastinput) < maxdepth-1:
    lastinput = lastinput + input
else:
    lastinput = lastinput[1:] + input