# state = recent history
# hist[state substring] = opponent most recent response
# use longest substring present in hist to build next throw
import random

if input == "":
    hist={}
    last=""
    ply=10
    minlen=3
    beats = {"R": "P", "P": "S", "S": "R"}
else:
    # record ONLY THIS RESPONSE in hist[state substring]
    for i in range(minlen, len(last)+1):
        hist[last[:i]] = input

    # update state
    last=output+input+last
    if len(last) > ply:
        last=last[:ply]

# look for state in history, play accordingly
try:
    max_seen = last[:max(i for i in range(minlen,len(last)+1) if last[:i] in hist)]
    output = beats[hist[max_seen]]
except:  # none seen
    output = random.choice("RPS")