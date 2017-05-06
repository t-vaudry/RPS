#By David Catt 2013.
import random
RPSID = ["R", "P", "S"]
RPSWIN = [1, 2, 0]
RPSLOSE = [2, 0, 1]
IMID = 2147483648
IMAX = 4294967295
class RPSMDL:
    def __init__(self, order, adapt):
        self.mask = 4**order
        self.ctx = 0
        self.rate = adapt
        self.mdl = [[IMID] * 3] * self.mask
        self.mask -= 1
    def predict(self):
        return self.mdl[self.ctx]
    def update(self, val, newm):
        val %= 3
        self.mdl[self.ctx][val] += (IMAX - self.mdl[self.ctx][val]) >> self.rate
        self.mdl[self.ctx][RPSWIN[val]] -= self.mdl[self.ctx][RPSWIN[val]] >> (self.rate + 1)
        self.mdl[self.ctx][RPSLOSE[val]] -= self.mdl[self.ctx][RPSLOSE[val]] >> (self.rate + 1)
        self.ctx = ((self.ctx << 2) ^ val) & self.mask;
        if newm == 1:
            self.ctx = self.mask
        

class RPSPREDICTOR:
    def __init__(self):
        self.model = RPSMDL(6, 2)
    def predict(self):
        tmp = self.model.predict()
        if tmp[0] > tmp[1]:
            if tmp[0] > tmp[2]:
                return 0
            else:
                return 2
        else:
            if tmp[2] > tmp[1]:
                return 2
            else:
                return 1
    def update(self, val, newg):
        self.model.update(val, newg)

        
if input == "":
    predictor = RPSPREDICTOR()
    aic = 0
elif input == "R":
    predictor.update(0, aic != 0)
elif input == "P":
    predictor.update(1, aic != 1)
elif input == "S":
    predictor.update(2, aic != 2)
aic = RPSWIN[predictor.predict()]
output = RPSID[aic]