#DC2SM (RPS_AI 1.6)
#By David Catt 2013.  Translated from C code.
import random
RPSID = ["R", "P", "S"]
RPSWIN = [1, 2, 0]
RPSLOSE = [2, 0, 1]
IMID = 2147483648
IMAX = 4294967295
class RPSMDL:
    def __init__(self, order, adapt, sense):
        self.mod = 3**order
        self.ctx = 0
        self.ptr = 0
        self.adaptive = adapt
        self.detectnum = sense
        self.match = 0
        if adapt == 0:
            self.mdl = [[0] * 3] * self.mod
        else:
            self.mdl = [[IMID] * 3] * self.mod
    def predict(self):
        return self.mdl[self.ptr]
    def update(self, val, newm):
        val %= 3
        if self.adaptive == 1:
            self.mdl[self.ptr][val] += (IMAX - self.mdl[self.ptr][val]) >> 4
            self.mdl[self.ptr][RPSWIN[val]] -= self.mdl[self.ptr][RPSWIN[val]] >> 5
            self.mdl[self.ptr][RPSLOSE[val]] -= self.mdl[self.ptr][RPSLOSE[val]] >> 5
        else:
            self.mdl[self.ptr][val] += 1
        self.ctx = ((self.ctx * 3) + val) % self.mod;
        if newm == 1:
            self.match = 0
        else:
            self.match += 1
        if self.detectnum == 1:
            self.ptr = self.ctx * 3
            if self.match == 0:
                self.ptr += 0
            elif self.match < 4:
                self.ptr += 1
            else:
                self.ptr += 2
            self.ptr %= self.mod
        else:
            self.ptr = self.ctx

class RPSPREDICTOR:
    def __init__(self, maxord):
        self.models = [[RPSMDL(0, 0, 0)] * 2] * maxord
        self.weights = [[IMID] * 2] * maxord
        self.last = [[0] * 2] * maxord
        self.maxord = maxord
        for o in range(0, self.maxord - 1):
            for a in range(0, 1):
                self.models[o][a] = RPSMDL(o, a, 0)
    def predict(self):
        tmp = [0, 0, 0]
        tot = 0
        ratios = [0.0, 0.0, 0.0]
        for o in range(0, self.maxord - 1):
            for a in range(0, 1):
                tmp = self.models[o][a].predict()
                tot = tmp[0] + tmp[1] + tmp[2]
                tot *= (10240000 / self.weights[o][a])
                if tot < 2:
                    tot *= 3
                if tot == 0:
                    tot = 1
                ratios[0] += tmp[0] / tot
                ratios[1] += tmp[1] / tot
                ratios[2] += tmp[2] / tot
                if tmp[0] > tmp[1]:
                    if tmp[0] > tmp[2]:
                        self.last[o][a] = 0
                    else:
                        self.last[o][a] = 2
                else:
                    if tmp[2] > tmp[1]:
                        self.last[o][a] = 2
                    elif tmp[0] == tmp[1] and tmp[1] == tmp[2]:
                        self.last[o][a] = random.choice([0, 1, 2])
                    else:
                        self.last[o][a] = 1
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
        for o in range(0, self.maxord - 1):
            for a in range(0, 1):
                self.models[o][a].update(val, 1)
                if val == self.last[o][a]:
                    self.weights[o][a] += (IMAX - self.weights[o][a]) >> 6
                else:
                    self.weights[o][a] -= self.weights[o][a] >> 7

        
if input == "":
    predictor = RPSPREDICTOR(12)
    aic = 0
elif input == "R":
    predictor.update(0)
elif input == "P":
    predictor.update(1)
elif input == "S":
    predictor.update(2)
aic = RPSWIN[predictor.predict()]
output = RPSID[aic]