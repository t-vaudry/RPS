#Created by David Catt on December 12, 2014
import random

class CtxModel:
    def __init__(self, order, decay):
        self.order = order
        self.decay = decay
        self.mask = 3 ** (order + 1)
        self.prob = [0.0] * self.mask
        self.ctx = 0
    def predict(self):
        tvl = 0
        tpr = 0.0
        prb = 0.0
        for i in range(0, 3):
            prb = self.prob[self.ctx + i]
            if prb > tpr:
                tvl = i
                tpr = prb
        return tvl#, tpr
    def update(self, val):
        for i in range(0, 3):
            self.prob[self.ctx + i] *= self.decay
        self.prob[self.ctx + val] += 1.0
        self.ctx = ((self.ctx + val) * 3) % self.mask

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
    mdl = [CtxModel(i % 7, 0.93) for i in range(0, 14)]
    msse = ModelSwitch(43, 0.93)
    msse.setoffset(42, -0.1)
    lval = 0
else:
    val = nval[input]
    for i in range(0, 7):
        mdl[i].update(val)
        mdl[i+7].update(lval)
    msse.update(val)
pv = 0
for i in range(0, 14):
    pv = mdl[i].predict()
    msse.setvalue(i, pv)
    msse.setvalue(i + 14, winner[pv])
    msse.setvalue(i + 28, winner[winner[pv]])
msse.setvalue(42, random.randint(0, 2))
lval = winner[msse.predict()]
output = cval[lval]