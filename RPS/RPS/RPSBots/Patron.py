'''
Date: 04.05.13
Bot: Charlotte
Author: Patron

v2 Deconstruction of classes since they exceed 5 sec CPU limit.
A few adjustments to d, noise. Use of only History analysis.
It turns out function calls are also expensive.

Dedicated to Charlotte Gainsbourg '''

import random
from operator import itemgetter
from heapq import nlargest
rchoice = random.choice

X = ['R','P','S']
merge = dict([(a+b,str(X.index(a)*3+X.index(b))) for a in X for b in X])
split = dict([(str(X.index(a)*3+X.index(b)),a+b) for a in X for b in X])
price = {'RP':1, 'PS':1, 'SR': 1,
        'RR':0, 'PP':0, 'SS':0,
        'RS':-1, 'PR':-1, 'SP':-1}

def shift_by (move, k = 1):
    return X[(X.index(move)+k)%3]

if not input:
    history = ''
    mode = 'defense'
    score = 0
    N = 1
    selection = 'decayed'
    accuracy = dict([(i,0) for i in range(N*6)])    
    out = rchoice(X)
else:
    moves = dict([(i,rchoice(X)) for i in range(6)])
    if len(history) > 1:
        for l in range(min(len(history)-1, 15), 2, -1):
            part = history[-l:]
            idx = history.rfind(part,0,-1)
            if idx != -1:
                moves[0] = shift_by(split[history[idx+l]][0])
                moves[1] = shift_by(split[history[idx+l]][0],2)
                moves[2] = shift_by(split[history[idx+l]][0],1)
                moves[3] = shift_by(split[history[idx+l]][1])
                moves[4] = shift_by(split[history[idx+l]][1],2)
                moves[5] = shift_by(split[history[idx+l]][1],1)
                break

    for i in range(6):
        accuracy[i] += .9*price[input + moves[i]]
    
    history += merge[input+output]
    score += price[input+output]

    if len(history) < 5:
        mode = 'defense'
    elif score < -5:
        mode = 'attack'
    elif score > 5:
        mode = 'defense'
    else: mode = 'normal'

    moves = dict([(i,rchoice(X)) for i in range(6)])

    for l in range(min(len(history)-1, 15), 2, -1):
        part = history[-l:]
        idx = history.rfind(part,0,-1)
        if idx != -1:
            moves[0] = shift_by(split[history[idx+l]][0])
            moves[1] = shift_by(split[history[idx+l]][0],2)
            moves[2] = shift_by(split[history[idx+l]][0],1)
            moves[3] = shift_by(split[history[idx+l]][1])
            moves[4] = shift_by(split[history[idx+l]][1],2)
            moves[5] = shift_by(split[history[idx+l]][1],1)
            break

    if mode == 'defense':
        out = rchoice(X)
    elif mode == 'normal':
        k = max(accuracy, key = accuracy.get)
        out = moves[k]
    elif mode == 'attack':
        k = max(accuracy, key = accuracy.get)
        move = moves[k]
        out = rchoice([s for s in X if s != move])

    if random.random() <= 0.3:
        out = rchoice(X)

output = out