#By David Catt 2013.
RPSID = ["R", "P", "S"]
RPSWIN = [1, 2, 0]
RPSLOSE = [2, 0, 1]
IMID = 2147483648
IMAX = 4294967295

class RPSPREDICTOR:
    def __init__(self):
        self.models = [[[IMID] * 3] * 3] * 2
        self.ctx = 0
    def predict(self):
        ratios = [0, 0, 0]
        ratios[0] = self.models[0][self.ctx][0] + self.models[1][self.ctx][0]
        ratios[1] = self.models[0][self.ctx][1] + self.models[1][self.ctx][1]
        ratios[2] = self.models[0][self.ctx][2] + self.models[1][self.ctx][2]
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
        self.models[0][self.ctx][val] += (IMAX - self.models[0][self.ctx][val]) >> 2;
        self.models[0][self.ctx][RPSWIN[val]] -= self.models[0][self.ctx][RPSWIN[val]] >> 3;
        self.models[0][self.ctx][RPSLOSE[val]] -= self.models[0][self.ctx][RPSLOSE[val]] >> 3;
        self.models[1][self.ctx][val] += (IMAX - self.models[1][self.ctx][val]) >> 6;
        self.models[1][self.ctx][RPSWIN[val]] -= self.models[1][self.ctx][RPSWIN[val]] >> 7;
        self.models[1][self.ctx][RPSLOSE[val]] -= self.models[1][self.ctx][RPSLOSE[val]] >> 7;
        self.ctx = val % 3

if input == "":
    predictor = RPSPREDICTOR()
elif input == "R":
    predictor.update(0)
elif input == "P":
    predictor.update(1)
elif input == "S":
    predictor.update(2)
aic = RPSWIN[predictor.predict()]
output = RPSID[aic]