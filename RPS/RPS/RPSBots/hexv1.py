import random

if not input:
    inputs = ""
    outputs = ""
    output = random.choice(['R','P','S'])
    beat = {'R':'P','P':'S','S':'R'}

else:
    inputs += input
    r, p = inputs.count('R'), inputs.count('P')
    s = len(inputs)
    gen = random.randint(1,s)
    if gen < r:
        output = beat['R']
    elif gen < r+p:
        output = beat['P']
    else:
        output = beat['S']

outputs += output