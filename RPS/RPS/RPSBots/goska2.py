import random

class RPS:
    def __init__(self):
        self.num = 0
        self.statistika = [0 for x in range(6)]
        self.strat = [True for x in range(6)]
        #0 kamen
        #1 skarje
        #2 papir
        #3 isto kot jaz
        #4 uno k jst premagam
        #5 uno k mene premaga
        ##6 ne isto kt jst
        self.mojCur = -1
        self.mojPrev = -1
        self.hisPrev = -1
    def procHisLast(self):
        #print 'njegovo, mojeP, mojCur', self.hisPrev, self.mojPrev, self.mojCur
        self.num += 1
        njegovo = self.hisPrev
        moje = self.mojCur
        if njegovo == 0: self.statistika[0] += 1
        elif njegovo == 1: self.statistika[1] += 1
        else: self.statistika[2] += 1
        if njegovo == moje: self.statistika[3] += 1
        elif njegovo == (moje+1)%3:
            self.statistika[4] += 1
            #self.statistika[6] += 1
        else:
            self.statistika[5] += 1
            #self.statistika[6] += 1
        #procesera tabelo booleanov
        if self.strat.count(True) == 1:
            d = self.strat.index(True)
            if d < 3 and self.statistika[d] != self.num:
                self.strat[self.strat.index(True)] = False 
            elif self.statistika[d] != self.num:
                self.strat[self.strat.index(True)] = False 
                
        else:
            for i in range(3):
                if self.statistika[i] != self.num:
                    self.strat[i] = False
            for i in range(3, 6):
                if self.statistika[i] != self.num:
                    self.strat[i] = False
    def converti(self, inp):
        if inp == 'R': return 0 #kamen, rock
        elif inp == 'S': return 1 #Scissors, skarje
        else: return 2
    def converto(self, out):
        if out == 0: return 'R'
        elif out == 1: return 'S'
        else: return 'P'
    def getOut(self):
        #print self.num, self.statistika, self.strat
        if self.strat.count(True) == 1:
            a = self.strat.index(True)
            if a < 3:
                return (a-1)%3
            elif a == 3: return (self.mojCur-1)%3
            elif a == 4: return self.mojCur
            else: return (self.mojCur+1)%3
        else:
            #print 'returnam random'
            return random.randint(0,2)
    def play_v_h_test(self):
        b = random.randint(0,2)
        self.mojCur = b
        self.mojPrev = b
        print self.converto(b)
        while True:
            self.hisPrev = self.converti(raw_input())
            #print '--'
            self.procHisLast()
            b = self.getOut()
            self.mojPrev = self.mojCur
            self.mojCur = b
            print self.converto(b)
    def play_rpscont1(self):
        b = random.randint(0,2)
        self.mojCur = b
        self.mojPrev = b
        return self.converto(b)
    def play_rpscont2(self, i):
        self.hisPrev = self.converti(i)
        self.procHisLast()
        b = self.getOut()
        self.mojPrev = self.mojCur
        self.mojCur = b
        return self.converto(b)
        
#### moje = od programa
#Igra = RPS()
#Igra.play_v_h_test()
#Igra.play_rpscont()


###tle je za rps contest.com ###
if input == '':
    Igra = RPS()
    output = Igra.play_rpscont1()
else:
    output = Igra.play_rpscont2(input)