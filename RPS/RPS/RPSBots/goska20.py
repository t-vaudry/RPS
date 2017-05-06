import random

class RPS:
    def __init__(self, n = 10):
        self.n = n #kok more bit neka zadeva zanesljiva da jo sprejmemo kot strategijo
        self.num = 0
        self.statistika = [0 for x in range(3)] + [0 for x in range(5)]
        self.strat = [True for x in range(8)]
        #0 kamen
        #1 skarje
        #2 papir
        #3 isto kot jaz
        #4 uno k jst premagam
        #5 uno k mene premaga
        #6 uno k bi on premagu
        #7 uno k bi njega premagal
        self.mojPrev = -1
        self.hisPrev = -1
        self.mojPrev2 = -1
        self.hisPrev2 = -1
    def procHisLast(self):
        n = self.n
        #print 'njegovo, njegovo2, moje', self.hisPrev, self.hisPrev2, self.mojPrev
        self.num += 1
        njegovo = self.hisPrev
        njegovo2 = self.hisPrev2
        moje = self.mojPrev2
        gorDol =  [False for x in range(8)]
        if njegovo == 0:
            gorDol[0] = True
        elif njegovo == 1:
            gorDol[1] = True
        else:
            gorDol[2] = True
        #
        if moje != -1:
            if njegovo == moje:
                gorDol[3] = True
            elif njegovo == (moje+1)%3:
                gorDol[4] = True
            else:
                gorDol[5] = True
        #
        if njegovo2 != -1:
            if njegovo == (njegovo2+1)%3:
                gorDol[6] = True
            elif njegovo == (njegovo2-1)%3:
                gorDol[7] = True
        #sprememba vrednosti statistike
        for i in range(8):
            if gorDol[i]:
                self.statistika[i] += 1
            else:
                self.statistika[i] = 0
        #procesera tabelo booleanov
        for i in range(8):
            if self.statistika[i] >= n:
                self.strat[i] = False
            else: self.strat[i] = True
        return
        #do sem je test
        if self.strat.count(True) == 1:
            d = self.strat.index(True)
            if self.statistika[d] != self.num:
                self.strat[self.strat.index(True)] = False        
        else:
            for i in range(8):
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
        print self.statistika
        if self.strat.count(True) != 0:
            n = random.randint(0,7)
            while not self.strat[n]:
                n = random.randint(0,7)
            a = n
            if a < 3:
                return (a-1)%3
            elif a == 3: return (self.mojPrev-1)%3
            elif a == 4: return self.mojPrev
            elif a == 5: return (self.mojPrev+1)%3
            elif a == 6: return (self.hisPrev)%3
            else: return (self.hisPrev+1)%3
        else:
            print 'random returnam',
            return random.randint(0,2)
    def play_v_h_test(self):
        b = random.randint(0,2)
        self.mojPrev = b
        print self.converto(b)
        while True:
            self.hisPrev2 = self.hisPrev
            self.hisPrev = self.converti(raw_input())
            self.procHisLast()
            #print '--', self.mojPrev, self.hisPrev, self.num,  self.statistika
            b = self.getOut()
            self.mojPrev2 = self.mojPrev
            self.mojPrev = b
            print self.converto(b)
    def play_rpscont1(self):
        b = random.randint(0,2)
        self.mojPrev = b
        return self.converto(b)
    def play_rpscont2(self, i):
        self.hisPrev2 = self.hisPrev
        self.hisPrev = self.converti(i)
        self.procHisLast()
        #print self.strat, self.statistika, self.num
        b = self.getOut()
        self.mojPrev2 = self.mojPrev
        self.mojPrev = b
        return self.converto(b)
        
#### moje = od programa
##Igra = RPS()
##Igra.play_v_h_test()


###tle je za rps contest.com ###
Igra = RPS()
o = Igra.play_rpscont1()
print o
##while True:
##    o = Igra.play_rpscont2(raw_input())
##    print '--'
##    print o


if input == '':
    Igra = RPS()
    o = Igra.play_rpscont1()
    output = o
else:
    o = Igra.play_rpscont2(input)
    output = o