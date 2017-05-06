# Rewritten recursive historian
# 
# 
import random

def findHist():
    for i in range(len(last), minlen-1, -1):
        if last[:i] in hist:
            (state, cache) = hist[last[:i]]
            for j in range(len(state),0,-1):
                if state[:j] in cache:
                    return cache[state[:j]]
            return state[1]
    return None

if input == "":  # init
    hist={}
    last=""
    ply=16
    minlen=3
    beats = {"R": "P", "P": "S", "S": "R"}
else:  # update history/state
    for i in range(len(last), minlen-1, -1):
        if last[:i] in hist:
            (state, cache) = hist[last[:i]]
            for j in range(len(state),0,-1):
                cache[state[:j]] = input
        else:  # never seen before
            (state, cache) = ("", {})
        hist[last[:i]] = ((output+input+state)[:ply], cache)
    last=(output+input+last)[:ply]

# look for state in history, play accordingly
output = findHist()
if output:
    output = beats[output]
else:
    output = random.choice("RPS")