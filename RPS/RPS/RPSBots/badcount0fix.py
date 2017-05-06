import random

#
#

def findmost(r, p, s):
    if r > s and r > p:
        return 3
    if s > r and s > p:
        return 2
    if p > r and p > s:
        return 1
    return 1

rndCnt = 1
rCnt = 0
sCnt = 0
pCnt = 0
if rndCnt < 51:
    whichout = random.randint(1,3)
    if whichout == 1:
        rCnt = rCnt + 1
        output = "R"
    if whichout == 2:
        pCnt = pCnt + 1
        output = "P"
    if whichout == 3:
        sCnt = sCnt + 1
        output = "S"

rndCnt = 50
whichout = findmost(rCnt, pCnt, sCnt)
if whichout == 1:
    rCnt = rCnt + 1
    output = "R"
if whichout == 2:
    pCnt = pCnt + 1
    output = "P"
if whichout == 3:
    sCnt = sCnt + 1
    output = "S"