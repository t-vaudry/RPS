import random

if input == '':
    numRR = 0
    numRP = 0
    numRS = 0
    numPR = 0
    numPP = 0
    numPS = 0
    numSR = 0
    numSP = 0
    numSS = 0
    lastinput = ''

if lastinput != '':
    twoinput = lastinput + input
    if twoinput == 'RR':
        numRR += 1
    elif twoinput == 'RP':
        numRP += 1
    elif twoinput == 'RS':
        numRS += 1
    elif twoinput == 'PR':
        numPR += 1
    elif twoinput == 'PP':
        numPP += 1
    elif twoinput == 'PS':
        numPS += 1
    elif twoinput == 'SR':
        numSR += 1
    elif twoinput == 'SP':
        numSP += 1
    else:
        numSS += 1

if input == 'R':
    numR = numRR
    numP = numRP
    numS = numRS
elif input == 'P':
    numR = numPR
    numP = numPP
    numS = numPS
else:
    numR = numSR
    numP = numSP
    numS = numSS
 
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
    
lastinput = input