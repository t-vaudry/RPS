# Converted from my old C++ program for this game...
#
# Versions
# ~~~~~~~~
#
#   1   -- not submitted.
#       -- original direct port that took too much time.
#          looks for repeated sequences and gives them weights.
#
#   2   -- submitted as "paper"
#       -- faster version of original alg, but with small fix, so beats v1.
#
#   3   -- submitted as "paper3"
#       -- changed to use max pattern length of 7 (was 10.)
#
#   3.2 -- submitted as "paper3.2"
#       -- changed to keep track of predictions from my moves and opponents
#          moves separately, and choose between them depending on the
#          win rate.  also added playing randomly if loosing badly.

import random

# globals for interfacing with the environment:
# [input] is the last move of the opponent, and it's empty if it is a new game.
# [output] is for our move.
# "R", "P", or "S".

MAX_LEN = 7
CAPTURE = {"R":"P", "P":"S", "S":"R"}

if input == "":
    # new game, reset stats
    cmvs = ""
    hmvs = ""
    cstats = {}
    hstats = {}
    wins = 0
    losses = 0
    count  = 0
    ccount = 1
    hcount = 1
else:
    # accumulate history of moves in the stats
    cmvs = _my_last_move + cmvs
    hmvs = input + hmvs

    ccount += (_my_last_cbest == input)
    hcount += (_my_last_hbest == input)
    count  += 1

    if _my_last_move == CAPTURE[input]:
        wins += 1
    else:
        losses += 1

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
cfreq = {"R":0, "P":0, "S":0}
hfreq = {"R":0, "P":0, "S":0}
for i in range(1, min(MAX_LEN, len(cmvs))):
    cpat = cmvs[:i]
    if cpat in cstats:
        cfreq["R"] += cstats[cpat]["R"]
        cfreq["S"] += cstats[cpat]["S"]
        cfreq["P"] += cstats[cpat]["P"]

    hpat = hmvs[:i]
    if hpat in hstats:
        hfreq["R"] += hstats[hpat]["R"]
        hfreq["S"] += hstats[hpat]["S"]
        hfreq["P"] += hstats[hpat]["P"]

#print freq

cbest = sorted(cfreq, key=lambda mv: cfreq[mv])[-1]
hbest = sorted(hfreq, key=lambda mv: hfreq[mv])[-1]

#if count == 999:
#    print ccount, hcount
#    #print ccount, "x", cbest, ":", hcount, "x", hbest

best = hbest if hcount >= ccount else cbest
#output = CAPTURE[best]
output = CAPTURE[best] if 100 * losses < 60 * count else random.choice("RSP")

_my_last_move = output
_my_last_cbest = cbest
_my_last_hbest = hbest