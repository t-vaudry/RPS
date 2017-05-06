##same as John debugged again, just different weights
import random
from time import sleep

class Igralec:
    ime = 'vpisi ime'
    def __init__(self):
        self.lama = 0.9 #lama = lambda
        self.prevm = 0
        self.prevh = 0
        self.prevm2 = 0
        self.prevh2 = 0
        self.hist = [[[20.0 for x in range(3)] for x in range(3)] for x in range(3)]
        #hist[MOJ PREJ%u0160NJI][NJEGOV PREJ%u0160NJI][REZULTAT]
    def update(self):
        for i in range(3):
            self.hist[self.prevm2][self.prevh2][i] *= self.lama
            if self.prevh == i:  self.hist[self.prevm2][self.prevh2][i] += 1
    def inflate(self, s):
        a = 1.0/sum(s)
        s = [x*a for x in s]
        return s
    def toSum(self, s):
        #iz seznama %u0161tevil naredi seznam, ki je pru %u010Dlen
        #pru %u010Dlen, drug %u010Dlen je drug %u010Dlen plus pru %u010Dlen,
        #tret %u010Dlen je pru plus drug plus tret %u010Dlen...
        for i in range(1,len(s)):
            s[i] = s[i] + s[i-1]
        return s
    def getHisNext(self):
        ver = self.toSum(self.inflate(list(self.hist[self.prevm][self.prevh])))
        hisNext = random.random()
        if hisNext < ver[0]:
            return 0
        elif hisNext < ver[1]:
            return 1
        else:
            return 2
    def poteza(self, tocke, prev): #for competition
        if prev == 'XX' or prev == ('X', 'X'):
            a = random.choice(['K', 'S', 'P'])
            self.prevm = self.stToin(a)
            return a
        self.prevh2 = self.prevh
        self.prevh = self.stToin(prev[1])
        ### kle se neha prev, delamo naprej
        self.update()
        self.prevm2 = self.prevm
        self.prevm = self.beat(self.getHisNext())
        return self.inTost(self.prevm)
    def rpscontINIT(self):
        return self.sloToEng(self.poteza(0, 'XX'))
    def rpscont(self, pr):
        return self.sloToEng(self.poteza(0, 'X' + self.engToSlo(pr)))
	### dit-like funkcije ###
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
# a = Igralec()
# mp2 = ''
# mr = 'K'
# mp = a.poteza(0, 'XX')
# from time import sleep
# for i in range(1000):
    # #print 'mm', mp2, mp
    # mp2 = mp
    # mp = a.poteza(0, mp+mr)
    # mr = mp2
    # sleep(0.1)
    # print 'delam',
# print 1/0

#konc testa
if input == '':
    a = Igralec()
    output = a.rpscontINIT()
    print output
else:
    output = a.rpscont(input)
    print output