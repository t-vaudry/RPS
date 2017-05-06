#Created by David Catt on December 12, 2014
import random

class CtxMap:
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
        return tvl
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
    amdl = [CtxMap(i % 7) if i < 14 else CtxMap((i % 7) * 2) for i in range(0, 19)]
    omdl = [CtxModel(i % 7, 0.93) if i < 14 else CtxModel((i % 7) * 2, 0.93) for i in range(0, 19)]
    msse = ModelSwitch(115, 0.93)
    msse.setoffset(114, -0.1)
    lval = 0
else:
    val = nval[input]
    for i in range(0, 7):
        amdl[i].update(val)
        amdl[i+7].update(lval)
        omdl[i].update(val)
        omdl[i+7].update(lval)
    for i in range(14, 19):
        amdl[i].update(val)
        amdl[i].update(lval)
        omdl[i].update(val)
        omdl[i].update(lval)
    msse.update(val)
pv = 0
for i in range(0, 19):
    pv = amdl[i].predict()
    msse.setvalue(i, pv)
    msse.setvalue(i + 19, winner[pv])
    msse.setvalue(i + 38, winner[winner[pv]])
    pv = omdl[i].predict()
    msse.setvalue(i + 57, pv)
    msse.setvalue(i + 76, winner[pv])
    msse.setvalue(i + 95, winner[winner[pv]])
msse.setvalue(114, random.randint(0, 2))
lval = winner[msse.predict()]
output = cval[lval]