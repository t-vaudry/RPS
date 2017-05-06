import random
if input=='':
    numR = 0
    numP = 0
    numS = 0
elif input=='R':
    numR+=1
elif input=='P':
    numP+=1
else:
    numS+=1

if numR > numP and numR > numS:
    output = 'P'
elif numP > numR and numP > numS:
    output = 'S'
elif numS > numR and numS > numP:
    output = 'R'
elif numR == numP and numP == numS:
    output = random.choice(['R','P','S'])
elif numR == numP:
    output = random.choice(['P','S'])
elif numR == numS:
    output = random.choice(['P','R'])
else:
    output = random.choice(['S','R'])