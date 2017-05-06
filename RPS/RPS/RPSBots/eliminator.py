#!/bin/python                                                                                                                                                                                                        
from pprint import pprint
from operator import itemgetter
from random import choice

#input = ""                                                                                                                                                                                                          

if not len(input):
    n_back = 3
    # moves = ""                                                                                                                                                                                                     
    moves = "PRSSPRPSPRPSPRPSPRPRPSRPSRPSRP"

moves += input

move_hash = {}

for i in range(len(moves)):
    cur = moves[i:i+n_back]

    if len(cur) < n_back: continue

    nxt = moves[i+n_back:i+n_back+1]

    if not len(nxt): continue

    # print cur, nxt                                                                                                                                                                                                 

    if not move_hash.has_key(cur):
        move_hash[cur] = {}

    if not move_hash[cur].has_key(nxt):
        move_hash[cur][nxt] = 0
    else:
        move_hash[cur][nxt] += 1

    # pprint(move_hash)                                                                                                                                                                                              

if len(input) and len(input) >= n_back:
    d = move_hash[moves[-n_back:]]
    prediction = sorted(d.items(), key=itemgetter(1))

    if prediction == "P":   output = "S"
    elif prediction == "R": output = "P"
    elif prediction == "S": output = "R"
else:
    output = choice(["R","P","S"])

moves = moves[-(n_back+1):]