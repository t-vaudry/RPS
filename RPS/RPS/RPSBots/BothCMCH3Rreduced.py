#Created by David Catt on December 12, 2014
import random

class CtxModel:
    def __init__(self, order):
        self.order = order
        self.mask = 3 ** order
        self.prob = [random.randint(0, 2) for a in range(0, self.mask)]
        self.ctx = 0
    def predict(self):
        return self.prob[self.ctx]
    def update(self, val):
        self.prob[self.ctx] = val
        self.ctx = ((self.ctx * 3) + val) % self.mask

class ModelSwitch:
    def __init__(self, count, decay):
        self.value = [1,0,-1,-1,1,0,0,-1,1]
        self.count = count
        self.decay = decay
        self.offset = [0.0] * count
        self.weigh = [0.0] * count
        self.pred = [0] * count
    def setoffset(self, idx, val):
        self.offset[idx] = val
    def setvalue(self, idx, val):
        self.pred[idx] = val
    def predict(self):
        tvl = 0
        tpr = -1.0
        prb = 0.0
        for i in range(0, self.count):
            prb = self.weigh[i] + self.offset[i]
            if prb > tpr:
                tvl = self.pred[i]
                tpr = prb
        return tvl
    def update(self, val):
        for i in range(0, self.count):
            self.weigh[i] = (self.weigh[i] * self.decay) + self.value[(val * 3) + self.pred[i]]

if input == "":
    winner = [1,2,0]
    nval = {"R":0,"P":1,"S":2}
    cval = ["R","P","S"]
    mdl = [CtxModel(i % 6) if i < 14 else CtxModel((i % 6) * 2) for i in range(0, 18)]
    msse = ModelSwitch(55, 0.93)
    msse.setoffset(54, -0.1)
    lval = 0
else:
    val = nval[input]
    for i in range(0, 6):
        mdl[i].update(val)
        mdl[i+12].update(val)
        mdl[i+6].update(lval)
        mdl[i+12].update(lval)
    msse.update(val)
pv = 0
for i in range(0, 18):
    pv = mdl[i].predict()
    msse.setvalue(i, pv)
    msse.setvalue(i + 18, winner[pv])
    msse.setvalue(i + 36, winner[winner[pv]])
msse.setvalue(54, random.randint(0, 2))
lval = winner[msse.predict()]
output = cval[lval]