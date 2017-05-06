# Noisy Historian
#
import random

def findPrecedent(state):
    for i in range(maxply, minply-1, -1):
        if state[:i] in HistCache:
            return HistCache[state[:i]]
    return None

if input == "":   # Historian Init
    HistCache={}
    last=""
    maxply=20
    minply=3
    beats = {"R": "P", "P": "S", "S": "R"}
    score = {'RR':0,'PP':0,'SS':0,'PR':1,'RS':1,'SP':1,'RP':-1,'SR':-1,'PS':-1}
    perf = 0
    badthresh = -7
    noiseLevel = 0.5
else:    # Update history, update state
    for i in range(minply, maxply+1):
        HistCache[last[:i]] = input
    last=(output+input+last)[:maxply]
    perf += score[output+input]  #  Track performance and adaptively get noisier when things are going poorly
    if perf < badthresh:
        noiseLevel *= 2
        perf = 0
    else:
        noiseLevel *= 0.99

prediction = findPrecedent(last)   # search history and play accordingly
if prediction and random.random() > noiseLevel:
    output = beats[prediction]
else:
    output = random.choice("RPS")