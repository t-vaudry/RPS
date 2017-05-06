# state = our last 10 moves
# if we've seen state before, beat whatever the most common next throw has been
# else random
#
# hist["PP"] = {"R":2, "P":0, "S":0} means both times we've thrown two
#     papers consecutively, the next throw from opponent was rock

import random

def beats(state):
    best=""
    beats = {"R": "P", "P": "S", "S": "R"}
    v= max(state.values())
    for i in state:
        if state[i] == v:
            best+=i
    return beats[random.choice(best)]

if input == "": # initialize
    hist={}
    last=""
    output=""

if (len(last) == 10): # if we have enough state
    if (last in hist): # if we've seen state before
        hist[last][input]+=1
    else: # have not seen state before
        hist[last] = {"R":0,"P":0,"S":0}
    last = last[1:]+output
else:
    last = last+output

if (len(last) == 10) and (last in hist): #mode 1
    output = beats(hist[last])
else:  #mode 2
    output = random.choice("RPS")