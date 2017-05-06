import random

class RPSPlayer:
    #               123456789.123456789.123456789.123456789.123456789.123456789.123456789.12
    DEFAULT_PLAY = "RSPRSPSSSSSSPSPRPPRPPSSPSSPPSSSPPRPPRPSPRSSSPSRRPRPSRPPRRSSSRRRPRRRRRSSP"
    SCORE = {"PR": 1, "RS": 1, "SP": 1, "RP": -1, "SR": -1, "PS": -1, "RR": 0, "SS": 0, "PP" : 0}
    
    KEYS = list(enumerate([[1,3,5,7], [2,4,6,8], [3,5,7], [4,6,8], [1,2,3,4], [2,3,4], [3,4]]))
   
    def __init__(self):
        self.round = 0
        self.hist_us = ""
        self.hist_them = ""
        self.memory = {}
        self.score = 0
        self.memory_length = 5

    def default_for_round(self):
        return self.DEFAULT_PLAY[self.round % 72]
        
    def tally_score(self):
        last_round = self.hist_us[-1:] + self.hist_them[-1:]
        #print last_round
        self.score += self.SCORE[last_round]
        
    def get_keys(self):
        def get_segment(s):
            # !!TODO suggests that it is about time to change this structure...
            if s == 1: return self.hist_them[len(self.hist_them) - 1]
            if s == 2: return self.hist_us  [len(self.hist_us  ) - 1]
            if s == 3: return self.hist_them[len(self.hist_them) - 2]
            if s == 4: return self.hist_us  [len(self.hist_us  ) - 2]
            if s == 5: return self.hist_them[len(self.hist_them) - 3]
            if s == 6: return self.hist_us  [len(self.hist_us  ) - 3]
            if s == 7: return self.hist_them[len(self.hist_them) - 4]
            if s == 8: return self.hist_us  [len(self.hist_us  ) - 4]
        
        for key_no, segment in self.KEYS:
            key = str(key_no) + ':'
            for s in segment:
                key += get_segment(s)
            yield key
    
    def remember_opponent(self, move):
        
        def add_key(key, move):
            # !!TODO forgetfullness so that
            # we do not get trained into a strategy...
            if key not in self.memory:
                 self.memory[key] = {"R": 0, "P": 0, "S": 0}
            self.memory[key][move] += 1
            #print self.hist_us
            #print self.hist_them
            #print key, move, self.memory[key]
        
        if len(self.hist_them) > self.memory_length:
            for key in self.get_keys():
                add_key(key, move)
        
        self.hist_them += move
        
        """if self.round % 10000 == 0:
           for key in self.memory:
               self.memory[key]["R"] /= 2
               self.memory[key]["P"] /= 2
               self.memory[key]["S"] /= 2"""
    
    def remember_me(self, move):
        self.hist_us += move

    def dump(self):
        print self.memory
        print self.hist_us
        print self.hist_them
        print "score", self.score
    
    def predict(self):
        
        def find(key):
            if key not in self.memory:
                 return {"R": 0, "P": 0, "S": 0}
            return self.memory[key]

        pr = pp = ps = 0
        for key in self.get_keys():
            value = find(key)  
            pr +=  value["R"]
            pp +=  value["P"]
            ps +=  value["S"]
        
        if pr == pp == ps == 0:
            return self.default_for_round()
        
        prediction = random.choice("R" * pr + "P" * pp + "S" * ps)
        
        if random.random() < 0.9:
            return {"R" : "P", "P" : "S", "S" : "R"}[prediction]
        else:
            return prediction

    def next(self, last_move):
        if last_move != "":
            self.remember_opponent(last_move)
            self.tally_score()
        if len(self.hist_us) < self.memory_length:
            result = self.default_for_round()
        else:
            result = self.predict()
        self.round += 1
        self.remember_me(result)
        return result


if input == "":
    player = RPSPlayer()

output = player.next(input)