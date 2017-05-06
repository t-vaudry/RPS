import random

if input == '':
    numR = 0
    numP = 0
    numS = 0
elif input == 'R':
    numR += 1
elif input == 'P':
    numP += 1
else:
    numS += 1
    
numR *= 0.95
numP *= 0.95
numS *= 0.95

Rscore = numS - numP
Pscore = numR - numS
Sscore = numP - numR
    
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