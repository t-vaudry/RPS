# author: mcstar at freemail dot hu
# upload: 1

from copy import deepcopy

def makeTable(rank):
    ten = [0 for _ in range(3)]
    while rank > 1:
        ten = [deepcopy(ten) for _ in range(3)]
        rank -= 1
    return ten

def listIndexInc(ten, indices, val):
    for i in indices[:-1]:
        ten = ten[i]
    ten[indices[-1]] += val

def listIndexGet(ten, indices):
    for i in indices:
        ten = ten[i]
    return ten
    
def argmax(lst):
    return lst.index(max(lst))

import random

def tr(c): return 0 if c == 'R' else 1 if c == 'P' else 2
def itr(c): return 'R' if c == 0 else 'P' if c == 1 else 'S'
def beat(c): return 'P' if c == 'R' else 'S' if c == 'P' else 'R'

ML = 5

if input == '':
    history_me = []
    history_op = []
    payoff = [[0,-1,1],[1,0,-1],[-1,1,0]]
    table_op = makeTable(ML)
    table_me = makeTable(ML)
    output = random.choice(['R','P','S'])
else:
    history_me.append(tr(output))
    history_op.append(tr(input))
    if len(history_op) >= ML:
        listIndexInc(table_op, history_op[-ML:], 1)
        listIndexInc(table_me, history_me[-ML:], 1)
    if len(history_op) < 50:
        output = random.choice(['R','P','S'])
    else:
        score = 0
        for me,op in zip(history_me[-10:], history_op[-10:]):
            score += payoff[me][op]
        if score < 2:
            output = beat(beat(itr(argmax(listIndexGet(table_me, history_me[-ML+1:])))))
        else:
            output = beat(itr(argmax(listIndexGet(table_op, history_op[-ML+1:]))))