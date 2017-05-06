#By David Catt 2013.
import random
RPSID = ["R", "P", "S"]
RPSWIN = [1, 2, 0]
RPSLOSE = [2, 0, 1]
IMID = 2147483648
IMAX = 4294967295
class RPSMDL:
    def __init__(self, order, adapt):
        self.mod = 3**order
        self.ctx = 0
        self.rate = adapt
        self.mdl = [[IMID] * 3] * self.mod
    def predict(self):
        return self.mdl[self.ctx]
    def update(self, val):
        val %= 3
        self.mdl[self.ctx][val] += (IMAX - self.mdl[self.ctx][val]) >> self.rate
        self.mdl[self.ctx][RPSWIN[val]] -= self.mdl[self.ctx][RPSWIN[val]] >> (self.rate + 1)
        self.mdl[self.ctx][RPSLOSE[val]] -= self.mdl[self.ctx][RPSLOSE[val]] >> (self.rate + 1)
        self.ctx = ((self.ctx * 3) + val) % self.mod;

class RPSPREDICTOR:
    def __init__(self, maxord, adapt):
        self.models = [RPSMDL(0, 0)] * (maxord + 1)
        self.weights = [IMID] * (maxord + 1)
        self.last = [0] * (maxord + 1)
        self.maxord = maxord
        self.rate = adapt
        for o in range(0, self.maxord):
            self.models[o] = RPSMDL(o, 4 - (o >> 1))
    def predict(self):
        tmp = [0, 0, 0]
        tot = 0
        ratios = [0.0, 0.0, 0.0]
        for o in range(0, self.maxord):
            tmp = self.models[o].predict()
            tot = tmp[0] + tmp[1] + tmp[2]
            if tot < 2:
                tot *= 3
            if tot == 0:
                tot = 1
            ratios[0] += (tmp[0] * self.weights[o] * (1.5**o)) / tot
            ratios[1] += (tmp[1] * self.weights[o] * (1.5**o)) / tot
            ratios[2] += (tmp[2] * self.weights[o] * (1.5**o)) / tot
            if tmp[0] > tmp[1]:
                if tmp[0] > tmp[2]:
                    self.last[o] = 0
                else:
                    self.last[o] = 2
            else:
                if tmp[2] > tmp[1]:
                    self.last[o] = 2
                elif tmp[0] == tmp[1] and tmp[1] == tmp[2]:
                    self.last[o] = random.choice([0, 1, 2])
                else:
                    self.last[o] = 1
        if ratios[0] > ratios[1]:
            if ratios[0] > ratios[2]:
                return 0
            else:
                return 2
        else:
            if ratios[2] > ratios[1]:
                return 2
            else:
                return 1
    def update(self, val):
        for o in range(0, self.maxord):
            self.models[o].update(val)
            if val == self.last[o]:
                self.weights[o] += (IMAX - self.weights[o]) >> self.rate
            else:
                self.weights[o] -= self.weights[o] >> (self.rate + 1)

        
if input == "":
    predictor = RPSPREDICTOR(6, 4)
    aic = 0
elif input == "R":
    predictor.update(0)
elif input == "P":
    predictor.update(1)
elif input == "S":
    predictor.update(2)
aic = RPSWIN[predictor.predict()]
output = RPSID[aic]