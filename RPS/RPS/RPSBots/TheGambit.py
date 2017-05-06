import random

gambits = [
    ['R','R','R'],
    ['P','P','P'],
    ['P','S','R'],
    ['R','S','P'],
    ['R','P','P'],
    ['P','S','S'],
    ['P','S','P'],
    ['S','S','S']
]

if not input:
    gambit = gambits[random.randint(0,len(gambits)-1)]
    curround = 0
    
output = gambit[curround]

curround += 1

if curround > 2:
    gambit = gambits[random.randint(0,len(gambits)-1)]
    curround = 0