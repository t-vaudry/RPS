import random

class RPSPlayer:
    #               123456789.123456789.123456789.123456789.123456789.123456789.123456789.12
    DEFAULT_PLAY = "RSPRSPSSSSSSPSPRPPRPPSSPSSPPSSSPPRPPRPSPRSSSPSRRPRPSRPPRRSSSRRRPRRRRRSSP"
    SCORE = {"PR": 1, "RS": 1, "SP": 1, "RP": -1, "SR": -1, "PS": -1, "RR": 0, "SS": 0, "PP" : 0}
    
    def __init__(self):
        self.round = 0
        self.hist = ""
        self.memory = {}
        self.score = 0

    def default_for_round(self):
        return self.DEFAULT_PLAY[self.round % 72]
        
    def tally_score(self):
        last_round = self.hist[-2:]
        #print last_round
        self.score += self.SCORE[last_round]
    
    def remember_opponent(self, move):
        
        def add_key(key, move):
            # not sure. add forgetfullness so that
            # we do not get trained into a strategy...
            if key not in self.memory:
                 self.memory[key] = {"R": 0, "P": 0, "S": 0}
            self.memory[key][move] += 1
        
        # I am a goldfish...
        if len(self.hist) >= 8:
            key = self.hist[-7:][:6]
            add_key("U" + key[0] + key[2] + key[4], move)
            add_key("T" + key[1] + key[3] + key[5], move)
        
        self.hist += move
    
    def remember_me(self, move):
        self.hist += move

    
    def dump(self):
        print self.memory
        print self.hist
        print "score", self.score
    
    def predict(self):
        
        def find(key):
            if key not in self.memory:
                 return {"R": 0, "P": 0, "S": 0}
            return self.memory[key]

        key = self.hist[-7:][:6]
        us    = find("T" + key[0] + key[2] + key[4]) 
        them  = find("U" + key[1] + key[3] + key[5])
       
        pr =  them["R"] + random.randint(0,4) + us["R"]
        pp =  them["P"] + random.randint(0,4) + us["P"]
        ps =  them["S"] + random.randint(0,4) + us["S"]
        
        if pr == pp == ps == 0:
            return self.default_for_round()
        
        prediction = random.choice("R" * pr + "P" * pp + "S" * ps)
        return {"R" : "P", "P" : "S", "S" : "R"}[prediction]

    def next(self, last_move):
        if last_move != "":
            self.remember_opponent(last_move)
            self.tally_score()
        if len(self.hist) < 6:
            result = self.default_for_round()
        else:
            result = self.predict()
        self.round += 1
        self.remember_me(result)
        return result



if input == "":
    player = RPSPlayer()

output = player.next(input)