# q-learning
import random

def getReward(matchup):
    lookup = {"RR":0, "RP":-1, "RS":1, 
              "PR":1, "PP":0, "PS":-1, 
              "SR":-1, "SP":1, "SS":0}
    return lookup[matchup]

def getNewValue(old, reward):
    return (((old + 0.9) * (0.9 * reward)) - old)

if input == "":
    _round = 0
    output = ""
    key = ''
    r = {}
    p = {}
    s = {}
    state = ["R","P","S"]
else:
    match = ''.join((output, input));
    if output == "R":
         r[key] = getNewValue(r[key], getReward(match))
    elif output == "P":
         p[key] = getNewValue(p[key], getReward(match))
    elif output == "S":
         s[key] = getNewValue(s[key], getReward(match))
    state[_round % 3] = input

key = ''.join(state)
    
if r.has_key(key):
    if r[key] > p[key] and r[key] > s[key]:
         output = "R"
    elif p[key] > s[key]:
         output = "P"
    else:
         output = "S"
else:
    r[key] = 0
    p[key] = 0
    s[key] = 0
    output = random.choice(["R", "P", "S"])

_round += 1