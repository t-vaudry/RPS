import random

CHOICE_TO_STRING = ['R', 'P', 'S']
STRING_TO_CHOICE = {'R': 0, 'P': 1, 'S': 2}

MEM = [0] * 9
M = []
J = []

if input == '':
    o = random.choice([0,1,2])
else:
    J.append(STRING_TO_CHOICE[input])
    if len(J)<2:
        o = random.choice([0,1,2])
    else:
        MEM[M[-2] * 3 + J[-2]] = J[-1]
        o = (MEM[M[-1] * 3 + J[-1]] + 1) % 3

M.append(o)
output = CHOICE_TO_STRING[o]