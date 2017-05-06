# author: blue-tomato
#
# bug-fix for frequencies-at-depth-4

import random

if input == '':
    num = {}
    lastinput = ''

numR = 0
numP = 0
numS = 0
if len(lastinput) == 3:
    manyin = lastinput + input
    if manyin in num:
        num[manyin] += 1
    else:
        num[manyin] = 1
    
    x = manyin[1:]+'R'
    if x in num:
        numR = num[x]
    x = manyin[1:]+'P'
    if x in num:
        numP = num[x]
    x = manyin[1:]+'S'
    if x in num:
        numS = num[x]

if numR > numP and numR > numS:
    output = 'P'
elif numP > numR and numP > numS:
    output = 'S'
elif numS > numR and numS > numP:
    output = 'R'
elif numR == numP and numP == numS:
    output = random.choice(['R','P','S'])
elif numR == numP:
    output = 'P'
elif numR == numS:
    output = 'R'
else:
    output = 'S'

if len(lastinput) < 3:
    lastinput = lastinput + input
else:
    lastinput = lastinput[1:] + input