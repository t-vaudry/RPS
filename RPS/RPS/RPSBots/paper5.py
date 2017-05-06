# Converted from my old C++ program for this game...
#
# Versions
# ~~~~~~~~
#
#   v1  -- not submitted.
#       -- original direct port that took too much time.
#          looks for repeated sequences and gives them weights.
#
#   v2  -- submitted as "paper"
#       -- faster version of original alg, but with small fix, so beats v1.
#
#   v3  -- submitted as "paper3"
#       -- changed to use max pattern length of 7 (was 10.)
#
#   v4  -- submitted as "paper4"
#       -- changed history degradation system.
#
#   v5  -- submitted as "paper5"
#       -- put back the weighting of pattern by length of pattern.  still has the
#          other aspects of v4's historical weight degradation.

import random

# globals for interfacing with the environment:
# [input] is the last move of the opponent, and it's empty if it is a new game.
# [output] is for our move.
# "R", "P", or "S".

MAX_LEN = 7
DEGRADE = 0.9

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
            cstats[cpat] = {"R":[0, len(cmvs)], "P":[0, len(cmvs)], "S":[0, len(cmvs)]}
        item = cstats[cpat][input]
        item[0] = (i + 1) + item[0] * DEGRADE**(len(cmvs) - item[1])
        item[1] = len(cmvs)

        hpat = hmvs[1:2 + i]
        if hpat not in hstats:
            hstats[hpat] = {"R":[0, len(hmvs)], "P":[0, len(hmvs)], "S":[0, len(hmvs)]}
        item = hstats[hpat][input]
        item[0] = (i + 1) + item[0] * DEGRADE**(len(hmvs) - item[1])
        item[1] = len(hmvs)

    #print cmvs
    #print hmvs
    #print cstats
    #print hstats

# chose move given stats
freq = {"R":0, "P":0, "S":0}
for i in range(1, min(MAX_LEN, len(cmvs))):
    cpat = cmvs[:i]
    if cpat in cstats:
        freq["R"] += cstats[cpat]["R"][0] * DEGRADE**(len(cmvs) - cstats[cpat]["R"][1])
        freq["S"] += cstats[cpat]["S"][0] * DEGRADE**(len(cmvs) - cstats[cpat]["S"][1])
        freq["P"] += cstats[cpat]["P"][0] * DEGRADE**(len(cmvs) - cstats[cpat]["P"][1])

    hpat = hmvs[:i]
    if hpat in hstats:
        freq["R"] += hstats[hpat]["R"][0] * DEGRADE**(len(hmvs) - hstats[hpat]["R"][1])
        freq["S"] += hstats[hpat]["S"][0] * DEGRADE**(len(hmvs) - hstats[hpat]["S"][1])
        freq["P"] += hstats[hpat]["P"][0] * DEGRADE**(len(hmvs) - hstats[hpat]["P"][1])

#print freq

best = sorted(freq, key=lambda mv: freq[mv])[-1]
output = {"R":"P", "P":"S", "S":"R"}[best]
_my_last_move = output