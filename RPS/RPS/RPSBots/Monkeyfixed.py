#Created by David Catt (2013)
#Finds the patterns most probable to win and uses them
import random
class monkey:
    def __init__(self, order):
        self.order = order
        self.size = 3**order
        self.actions = [[0.0,0.0,0.0] for a in range(self.size)]
    def tally(self, ctx, rslt):
        self.actions[ctx % self.size][rslt] += 1.0
    def getbest(self):
        bestp = 0.5
        bests = random.randint(0, self.size - 1)
        thisp = 0.0
        total = 0.0
        for i in range(0, self.size - 1):
            total = self.actions[i][0] + self.actions[i][1] + self.actions[i][2]
            if total == 0:
                thisp = 0.0
            else:
                thisp = (self.actions[i][2] + (self.actions[i][1] / 2.0)) / total
            if thisp > bestp:
                bestp = thisp
                bests = i
        return bests,bestp
    
if input == "":
    maxord = 3
    maxval = 3**maxord
    brains = [monkey(o) for o in range(0,maxord)]
    result = {"RR":1,"RP":0,"RS":2,"PR":2,"PP":1,"PS":0,"SR":0,"SP":2,"SS":1}
    chrval = {"R":0,"P":1,"S":2}
    valchr = ["R","P","S"]
    last = ""
    ctx = 0
    cur = 0
    pos = 0
else:
    for i in range(0, maxord - 1):
        brains[i].tally(ctx, result[last + input])
    ctx = ((ctx * 3) + chrval[last]) % maxval
if pos == 0:
    bestp = 0.5
    bests = random.randint(0, 2)
    besto = 1
    for i in range(0, maxord - 1):
        thiss,thisp = brains[i].getbest()
        if thisp > bestp:
            bestp = thisp
            bests = thiss
            besto = i + 1
    pos = besto
    cur = bests
pos -= 1
output = last = valchr[(cur / (3**pos)) % 3]