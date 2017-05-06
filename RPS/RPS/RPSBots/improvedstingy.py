# state = last [depth]-turn sequence, both players' moves
# if we've seen state before, throw to beat weighted-avg opponent throw
# else random

import random

if input == "": # initialize
    hist={}
    last=""
    output=""
    depth=5

# record state for last play + opponent response
if (len(last) == 2*depth): 
    if (last not in hist):
        hist[last] = ""
    hist[last]+=input

# update state
last+=output+input
if len(last) > 2*depth:
    last=last[2:]

# look for state in history, play accordingly
if last in hist:
    beats = {"R": "P", "P": "S", "S": "R"}
    output = beats[random.choice(hist[last])]
else:
    output = random.choice("RPS")