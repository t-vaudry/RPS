# Rating Decay Bot
# Uses ranking derived from current input, overall variable counts, and pattern recognition
# Ratings are decreased 20% per iteration, so current ratings have more weight than older ratings.
# 12/4/2013
#

import random
import math

buffer_Length = 8

if not input:
    # Initilization
    beat = {'R':'P','P':'S','S':'R'}
    encoding = { 'R': 0, 'P' : 1, 'S' : 2}
    rCtr = pCtr = sCtr = rLast = pLast = sLast = 0
    rRate = pRate= sRate = 0
    oppHistory = "" 
    histBuffer = ""
    searcher = ""
    output=random.choice(['R','P','S'])

else :
    #record current input
    oppHistory += str(encoding[input])
    rRate *= .8
    pRate *= .8
    sRate *= .8

    #update ratings based on input
    if input == "R":
        rCtr += 1
        rLast = 0
        pLast += 1
        sLast += 1
        pRate += 0.075
        sRate -= 0.075

    elif input == "P":
        pCtr += 1
        rLast += 1
        pLast = 0
        sLast += 1
        sRate += 0.075
        rRate -= 0.075

    elif input == "S":
        sCtr += 1
        rLast += 1
        pLast += 1
        sLast = 0
        rRate += 0.075
        pRate -= 0.075
   
    #increase the rating of the overall top used value
    if rCtr > sCtr and rCtr > pCtr :
        rRate += 0.05
    elif pCtr < rCtr and pCtr < sCtr :
        pRate += 0.05
    elif sCtr < rCtr and sCtr < pCtr :
        sRate += 0.05

    # check for same pattern in history
    histBuffer += str(encoding[input])
    if len(histBuffer)> buffer_Length :
        histBuffer = histBuffer[1:]
    
    idx = oppHistory.rfind(histBuffer, 0, -1)
    if idx != -1 :
        #pattern found so improve rating of RPS that would beat most likely to come next
        next = oppHistory[idx + 1]
        if next == encoding['R'] :
            pRate += 0.075
            sRate -= 0.075
        elif next == encoding['P'] :
            sRate += 0.075
            rRate -= 0.075
        elif next == encoding['S'] :
            rRate += 0.075
            pRate -= 0.075

    expRock = math.exp(rRate)
    expScissors = math.exp(sRate)
    expPaper = math.exp(pRate)

    #Determing the next move to be played from rankings
    Rating = random.random()* (expRock + expScissors + expPaper)
    if Rating < expRock:
        output = "R"
    elif Rating < (expRock + expPaper):
        output = "P"
    else:
        output = "S"