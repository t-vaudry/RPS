#it turned out that debug made a bigger bug than it repaired

import random
from time import sleep

class Igralec:
    def __init__(self):
        self.lama = 0.9 #lama = lambda
        self.prevm = 0
        self.prevh = 0
        self.prevm2 = 0
        self.prevh2 = 0
        self.hist = [[[1.0 for x in range(3)] for x in range(3)] for x in range(3)]
        #hist[MOJ PREJ%u0160NJI][NJEGOV PREJ%u0160NJI][REZULTAT]
    def update(self):
        print self.prevm, self.prevh
        for i in range(3):
            self.hist[self.prevm2][self.prevh2][i] *= self.lama
            if self.prevh == i:
                self.hist[self.prevm2][self.prevh2][i] += 1
    def inflate(self, s):
        a = 1.0/sum(s)
        s = [x*a for x in s]
        #print sum(s)
        return s
    def toSum(self, s):
        #iz seznama %u0161tevil naredi seznam, ki je pru %u010Dlen
        #pru %u010Dlen, drug %u010Dlen je drug %u010Dlen plus pru %u010Dlen,
        #tret %u010Dlen je pru plus drug plus tret %u010Dlen...
        for i in range(1,len(s)):
            s[i] = s[i] + s[i-1]
        return s
    def getHisNext(self):
        verjetnosti = self.toSum(self.inflate(list(self.hist[self.prevm][self.prevh])))
        print self.inflate(self.hist[self.prevm][self.prevh])[self.prevm]
        hisNext = random.random()
        if hisNext < verjetnosti[0]:
            return 0
        elif hisNext < verjetnosti[1]:
            return 1
        else:
            return 2
    def poteza(self, tocke, prev):
        #for competition
        if prev == 'XX':
            a = random.choice(['K', 'S', 'P'])
            self.prevm = self.stToin(a)
            return a
        self.prevh2 = self.prevh
        self.prevh = self.stToin(prev[1])
        ### kle se neha prev, delamo naprej
        #print prev
        self.update()
        self.prevm2 = self.prevm
        self.prevm = self.beat(self.getHisNext())
        return self.inTost(self.prevm)
    def rpscontINIT(self):
        return self.sloToEng(self.poteza(0, 'XX'))
##        a = random.choice(['R', 'S', 'P'])
##        self.prevm = self.stToin(a)
##        return a
    def rpscont(self, pr):
        return self.sloToEng(self.poteza(0, 'X' + self.engToSlo(pr)))
        #rspcont
##        self.prevh2 = self.prevh
##        self.prevh = self.stToin(self.engToSlo(pr))
##        self.update()
##        self.prevm2 = self.prevm
##        self.prevm = self.beat(self.getHisNext())
##        return self.sloToEng(self.inTost(self.prevm))
    ###Naslednje funkcije bi blo fajn zapisat v dict ###
    def inTost(self, a):
        if a == 0:
            return 'K'
        elif a == 1:
            return 'S'
        else:
            return 'P'
    def sloToEng(self, a):
        if a == 'K':
            return 'R'
        else:
            return a #P == P and S == S
    def engToSlo(self, a):
        if a== 'R':
            return 'K'
        else:
            return a
    def stToin(self, a):
        if a== 'K':
            return 0
        elif a == 'S':
            return 1
        else:
            return 2
    def beat(self, a):
        if a == 0:
            return 2
        elif a == 1:
            return 0
        else:
            return 1
    ###konc dit-like funkcij####
#test %u010De se%u0161tevanje deluje
##a = Igralec()
##mp2 = ''
##mr = 'K'
##mp = a.poteza(0, 'XX')
##for i in range(1000):
##    #print 'mm', mp2, mp
##    mp2 = mp
##    mp = a.poteza(0, mp+mr)
##    mr = mp2
##    sleep(0.1)
##print 1/0
#konc testa
if input == '':
    a = Igralec()
    output = a.rpscontINIT()
    print output
else:
    output = a.rpscont(input)
    print output
##a = Igralec()
##print a.poteza(0, 'XX')
##print a.poteza(1, 'PS')
##for i in a.hist:
##    for j in i:
##        print j