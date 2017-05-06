# converted from my old C++ program for this game...

import random

# globals for interfacing with the environment:
# [input] is the last move of the opponent, and it's empty if it is a new game.
# [output] is for our move.
# "R", "P", or "S".

MAX_LEN = 7

if input == "":
    # new game, reset stats
    cmvs = ""
    hmvs = ""
    cstats = {}
    hstats = {}
else:
    # accumulate history of moves in the stats
    cmvs = _my_last_move + cmvs
    hmvs = input + hmvs

    for i in range(min(MAX_LEN, len(cmvs) - 1)):
        cpat = cmvs[1:2 + i]
        if cpat not in cstats:
            cstats[cpat] = {"R":0, "P":0, "S":0}
        cstats[cpat][input] += (i + 1) * len(cmvs)

        hpat = hmvs[1:2 + i]
        if hpat not in hstats:
            hstats[hpat] = {"R":0, "P":0, "S":0}
        hstats[hpat][input] += (i + 1) * len(hmvs)

    #print cmvs
    #print hmvs
    #print cstats
    #print hstats

# chose move given stats
freq = {"R":0, "P":0, "S":0}
for i in range(1, min(MAX_LEN, len(cmvs))):
    cpat = cmvs[:i]
    if cpat in cstats:
        freq["R"] += cstats[cpat]["R"]
        freq["S"] += cstats[cpat]["S"]
        freq["P"] += cstats[cpat]["P"]

    hpat = hmvs[:i]
    if hpat in hstats:
        freq["R"] += hstats[hpat]["R"]
        freq["S"] += hstats[hpat]["S"]
        freq["P"] += hstats[hpat]["P"]

#print freq

best = sorted(freq, key=lambda mv: freq[mv])[-1]
output = {"R":"P", "P":"S", "S":"R"}[best]
_my_last_move = output