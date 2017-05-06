#http://robotypo.appspot.com

import random
        
class Robotypo1:
    name = "Robotypo1"
    
    def reset(self):
        self.SMOOTH = 30.0 / 100
        self.SMOOTH_MIN = 10.0 / 100
        self.SMOOTH_MAX = 80.0 / 100 
        self.ADJUSTMENT = 1 / 1000
        self.case3 = 0
        self.case2 = 0
        self.case1 = 0
        self.prob = []
        for i in range(729):
            self.prob.append([10000, 10000, 10000])

    def get_move(self):
        p = self.prob[self.case3 * 81 + self.case2 * 9 + self.case1];
        opp = self.findMax([random.randint(0, p[0]), random.randint(0, p[1]), random.randint(0, p[2])]);
        return self.anti_expected(self.hand_by_index(opp));
    
    def findMax(self, p):
        if p[0] >= p[1] and p[0] >= p[2]:
            return 0
        if p[1] >= p[2]:
            return 1
        return 2
    
    def anti_expected(self, expected):
        """Returns a winning move against the expected one"""
        return {None: 'P', 'R': 'P', 'P': 'S', 'S':'R'}[expected]

    def index(self, hand):
        return ['R', 'P', 'S'].index(hand)

    def hand_by_index(self, index):
        return ['R', 'P', 'S'][index]

    def inform_played(self, opp, my):

        oppIdx = self.index(opp)
        myIdx = self.index(my)
        
        self.case3 = self.case2
        self.case2 = self.case1
        self.case1 = myIdx * 3 + oppIdx
        p = self.prob[self.case3* 81 + self.case2 * 9 + self.case1]

        for i in range(3):
            d = 5000
            if oppIdx != i:
                d = 0
            p[i] = int(d * self.SMOOTH + p[i] * (1 - self.SMOOTH))
        if self.anti_expected(my) == opp and self.SMOOTH < self.SMOOTH_MAX:
            self.SMOOTH += self.ADJUSTMENT
        elif self.anti_expected(opp) == my and self.SMOOTH > self.SMOOTH_MIN:
            self.SMOOTH -= self.ADJUSTMENT
        
if input == '':
    bot = Robotypo1()
    bot.reset()
else:
    try:
        out = output
        if not out in ["R", "P", "S"]:
            raise
        bot.inform_played(input, out)
    except:
        pass

output = bot.get_move()