## hiddenSkillMk3.py
## This RPS program is designed to cloak it's
## strategy in randomness to confuse the opponent.
import random
def rand():
    return random.choice(['R','P','S'])
class Stats:
    def __init__(self):
        self.w = float(0)
        self.l = float(0)
        self.t = float(0)
    def analyze(self,opp,com):
        if opp==com:
            self.t+=1
        elif (opp=='R' and com=='P') or (opp=='P' and com=='S') or (opp=='S' and com=='R'):
            self.w+=1
        else:
            self.l+=1
    def winRatio(self):
        return (self.w+(self.t)/2)/(self.w+self.t+self.l)
class Predict:
    def __init__(self):
        self.r = 0
        self.p = 0
        self.s = 0
        self.t = 1
    def analyze(self,inp):
        
        if inp=='':
            return
        self.t+=1
        print self.t
        if inp=='R':
            self.r+=1
        elif inp=='P':
            self.p+=1
        else:
            self.s+=1
    def play(self):
        r = random.randint(1,self.t)
        if r<=self.r:
            return 'P'
        if r>=self.r+self.p:
            return 'R'
        return 'S'
if input=='':
    moves = 0
    mode = 'ANALYZE'
    a = Predict()
    prev = ''
    stats = Stats()
moves+=1
if mode=='ANALYZE':
    if moves==100:
        mode='TESTING'
        moves=0
    output = rand()
    a.analyze(input)
elif mode=='TESTING':
    if moves==150:
        if stats.winRatio()>0.45:
            mode='EXECUTION'
        else:
            mode='REANALYZATION'
            a = Predict()
        moves=0
    if random.choice([True,False]):
        output = rand()
    else:
        output = a.play()
    a.analyze(input)
elif mode=='REANALYZATION':
    if moves==50:
        mode=='TESTING'
        moves=0
    output = rand()
    a.analyze(input)
elif mode=='EXECUTION':
    if stats.winRatio()>0.7:
        mode = 'FREEZE'
    if stats.winRatio()<0.45:
        mode = 'REANALYZATION'
    output = a.play()
    a.analyze(input)
elif mode=='FREEZE':
    output = rand() #If it is winning by a lot, keep it that way.
stats.analyze(input,prev)
prev = output
print output