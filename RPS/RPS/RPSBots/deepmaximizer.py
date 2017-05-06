# author: blue-tomato
#
# analyzes the frequencies (with dynamic depth algorithm)
# attempts to maximize expected return

import random

if input == '':
    num = {}
    lastinput = ''
    maxdepth = 5
    randthresh = 1.1
    depthscore = [0.0,0.0,0.0,0.0,0.0]
    depthguess = ['','','','','']
else:
    for i in range(0,maxdepth):
        if input == 'R':
            if depthguess[i] == 'R':
                depthscore[i] += 1.0
            elif depthguess[i] != '':
                depthscore[i] -= 0.6667
        if input == 'P':
            if depthguess[i] == 'P':
                depthscore[i] += 1.0
            elif depthguess[i] != '':
                depthscore[i] -= 0.6667
        if input == 'S':
            if depthguess[i] == 'S':
                depthscore[i] += 1.0
            elif depthguess[i] != '':
                depthscore[i] -= 0.6667
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
        depthguess[i] = ''
    elif numR > numP and numR > numS:
        depthguess[i] = 'R'
    elif numP > numR and numP > numS:
        depthguess[i] = 'P'
    elif numS > numR and numS > numP:
        depthguess[i] = 'S'
    else:
        depthguess[i] = ''
        
Rstar = 0
Pstar = 0
Sstar = 0
if max(depthscore) > randthresh:
    for i in range(0,maxdepth):
        if depthscore[i] > 0:
            if depthguess[i] == 'R':
                Rstar += depthscore[i]
            if depthguess[i] == 'P':
                Pstar += depthscore[i]
            if depthguess[i] == 'S':
                Sstar += depthscore[i]

Rscore = Sstar - Pstar
Pscore = Rstar - Sstar
Sscore = Pstar - Rstar

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