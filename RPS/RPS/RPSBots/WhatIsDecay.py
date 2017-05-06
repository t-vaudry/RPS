#By David Catt 2013.
import random
RPSID = ["R", "P", "S"]
RPSWIN = [1, 2, 0]
RPSLOSE = [2, 0, 1]
class RPSMDL:
    def __init__(self, order, begin, decay):
        self.mod = 3**order
        self.ctx = 0
        self.rate = decay
        self.mdl = [[begin] * 3] * self.mod
    def predict(self):
        return self.mdl[self.ctx]
    def update(self, val):
        val %= 3
        self.mdl[self.ctx][0] *= self.rate
        self.mdl[self.ctx][1] *= self.rate
        self.mdl[self.ctx][2] *= self.rate
        self.mdl[self.ctx][val] += 1
        self.ctx = ((self.ctx * 3) + val) % self.mod;
        

class RPSPREDICTOR:
    def __init__(self):
        self.model = RPSMDL(3, 10.0, 0.92)
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
    def update(self, val):
        self.model.update(val)

        
if input == "":
    predictor = RPSPREDICTOR()
    aic = 0
elif input == "R":
    predictor.update(0)
elif input == "P":
    predictor.update(1)
elif input == "S":
    predictor.update(2)
aic = RPSWIN[predictor.predict()]
output = RPSID[aic]