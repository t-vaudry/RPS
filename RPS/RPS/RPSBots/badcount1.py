import random

#- - - - -
# by goodbad
# changes from badcount0fix to badcount1:
#   fixed bug where the program only played random numbers
#   findmost renamed to choosemove
#   choosemove returns a random result when there is a tie
#   bot now plays a random move 20% of the time
#- - - - -

# 10 percent chance to go on a random series of moves
# returns True if the chance is met, False otherwise
def playRandMove():
    chance = random.randint(1, 100)
    if chance <= 20:
        return True
    else:
        return False

def choosemove(r, p, s):
    if r > s and r > p:
        return 3
    if s > r and s > p:
        return 2
    if p > r and p > s:
        return 1
    return random.randint(1, 3)

if not input:
    rndCnt = 2
    rCnt = 0
    sCnt = 0
    pCnt = 0
    out = random.randint(1, 3)
    if out == 1:
        rCnt = rCnt + 1
        output = "R"
    if out == 2:
        pCnt = pCnt + 1
        output = "P"
    if out == 3:
        sCnt = sCnt + 1
        output = "S"
    
if rndCnt < 51:
    whichout = random.randint(1,3)
    if whichout == 1:
        rndCnt = rndCnt + 1
        rCnt = rCnt + 1
        output = "R"
    if whichout == 2:
        rndCnt = rndCnt + 1
        pCnt = pCnt + 1
        output = "P"
    if whichout == 3:
        rndCnt = rndCnt + 1
        sCnt = sCnt + 1
        output = "S"

if playRandMove():
    rout = random.randint(1, 3)
    if rout == 1:
        rCnt = rCnt + 1
        output = "R"
    if rout == 2:
        pCnt = pCnt + 1
        output = "P"
    if rout == 3:
        sCnt = sCnt + 1
        output = "S"

whichout = choosemove(rCnt, pCnt, sCnt)
if whichout == 1:
    rCnt = rCnt + 1
    output = "R"
if whichout == 2:
    pCnt = pCnt + 1
    output = "P"
if whichout == 3:
    sCnt = sCnt + 1
    output = "S"