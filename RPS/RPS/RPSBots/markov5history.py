import random
import itertools

output = ""
erpsROCK = 0
erpsPAPER = 1
erpsSCISSORS = 2

ErpsValues = [erpsROCK, erpsPAPER, erpsSCISSORS]

maperpserpsBeat = {
    erpsROCK: erpsPAPER,
    erpsPAPER: erpsSCISSORS,
    erpsSCISSORS: erpsROCK,
}

def Binomial(n, k):
    if k == 0:
        return 1
    elif 2*k > n:
        return Binomial(n,n-k)
    else:
        e = n-k+1
        for i in range(2,k+1):
            e *= (n-k+i)
            e /= i
        return e

class CMarkovChain:
    def __init__(self, nSteps):
        self.m_mapplaytransition = {}
        self.m_aplayHistory = ((-1,-1),) * nSteps
        self.m_erpsMinePrev = -1
    def RegisterOpponentsPreviousMove(self, erpsOpponentPrev):
        if self.m_aplayHistory not in self.m_mapplaytransition:
            self.m_mapplaytransition[self.m_aplayHistory] = [1, 1, 1] # pretend each transition happened at least once
        self.m_mapplaytransition[self.m_aplayHistory][erpsOpponentPrev] = self.m_mapplaytransition[self.m_aplayHistory][erpsOpponentPrev] + 1
        self.m_aplayHistory = self.m_aplayHistory[1:] + ((erpsOpponentPrev, self.m_erpsMinePrev),)
    def LooksRandom(self):
        """Determines how likely a random erps generator would produce the transition probabilities for current history"""
        if self.m_aplayHistory not in self.m_mapplaytransition:
            return 1 # if not enough data, we know nothing, so it looks random
        transition = self.m_mapplaytransition[self.m_aplayHistory]
        nTransitionCount = sum(transition)
        return (Binomial(nTransitionCount, transition[erpsROCK]) * Binomial(nTransitionCount-transition[erpsROCK], erpsPAPER)) / (len(ErpsValues)**nTransitionCount)
    def GenerateMyAnswer(self):
        erpsMine = -1 # must be initialized later
        if self.LooksRandom() < random.random():
            transition = self.m_mapplaytransition[self.m_aplayHistory]
            # generate bounds to choose a random erps according to distribution given by transition
            aintvlnBound = [() for erps in ErpsValues]
            nValuesProcessed = 0
            for erps in ErpsValues:
                aintvlnBound[erps] = (nValuesProcessed, nValuesProcessed + transition[erps])
                nValuesProcessed = nValuesProcessed + transition[erps]
            nRandomNumber = random.randint(0, sum(transition)-1) # randint inclusive on both ends
            # find respective choice
            for erps in ErpsValues:
                if aintvlnBound[erps][0] <= nRandomNumber and nRandomNumber < aintvlnBound[erps][1]:
                    assert(erpsMine==-1)
                    erpsMine = maperpserpsBeat[erps]
        else:
            erpsMine = random.choice(ErpsValues)
        assert(erpsMine!=-1) # erpsMine must be initialized
        self.m_erpsMinePrev = erpsMine
        return erpsMine
    def PrintMarkovChain(self):
        for play, transition in self.m_mapplaytransition.items():
            print("%s %s"%(str(play), str(transition)))

def InputToERPS(strIn):
    return { "R" : erpsROCK, "P" : erpsPAPER, "S" : erpsSCISSORS }[strIn]

def ERPSToOutput(erps):
    return { erpsROCK : "R", erpsPAPER : "P", erpsSCISSORS : "S" }[erps]

def Output(erps):
    global erpsMinePrev
    erpsMinePrev = erps # remember for later
    global output
    output = ERPSToOutput(erps)

def FirstRound():
    global markovchain
    markovchain = CMarkovChain(5)
    Output(markovchain.GenerateMyAnswer())

def LaterRound(erpsOpponentPrev):
    global markovchain
    markovchain.RegisterOpponentsPreviousMove(erpsOpponentPrev)
    # markovchain.PrintMarkovChain()
    Output(markovchain.GenerateMyAnswer())

if input=="":
    FirstRound()
else:
    LaterRound(InputToERPS(input))