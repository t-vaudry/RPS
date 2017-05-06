from collections import defaultdict
import operator
import random

class Bayes:
    name = "Bayes"

    def reset(self):
        self.score_table = { 
              ('P', 'P'): 1,
              ('P',  'S'): 0,
              ('P', 'R'): 3,

              ('S', 'P'): 3,
              ('S', 'S'): 1,
              ('S', 'R'): 0,
              
              ('R', 'P'): 0,
              ('R', 'S'): 3,
              ('R', 'R'): 1,
  
        }
        
        self.opplastm_probs = defaultdict(lambda: defaultdict(lambda: 0))
        self.mylastm_probs = defaultdict(lambda: defaultdict(lambda: 0))

        self.played_probs = defaultdict(lambda: 0)

        self.mylastm = None
        self.opplastm = None

    
    def train(self, played, opplm, mylastm):
        self.played_probs[played] += 1 
        self.opplastm_probs[opplm][played] += 1
        self.mylastm_probs[mylastm][played] += 1

    def guess_opp(self, opplm, mylm):
        probs = defaultdict(lambda: 0)
        for hand in ["R", "P", "S"]:
            probs[hand] = self.played_probs[hand] * self.opplastm_probs[opplm][hand] * self.mylastm_probs[mylm][hand] 
        return probs

    def counter(self, probs):
        weighted_list = []
        for h in ['R', 'P', 'S']:
            weighted = 0
            for p in probs.keys():
                points = self.score_table[(h, p)]
                prob = probs[p]
                weighted += points * prob

            weighted_list.append((h, weighted))

        return max(weighted_list, key=operator.itemgetter(1))[0]

    def get_move(self):
        if not (self.mylastm and self.opplastm):
            return random.choice(['R', 'P', 'S'])

        probs = self.guess_opp(self.opplastm, self.mylastm)
        counter = self.counter(probs)
        return counter

    def inform_played(self, opp, my):
        if self.mylastm and self.opplastm:
            self.train(opp, self.opplastm, self.mylastm)
        
        self.opplastm = opp
        self.mylastm = my 

    def endgame(self):
        pass

if input == '':
    bot = Bayes()
    bot.reset()
elif getattr(None, "output", None):
    bot.inform_played(input, ouput)

output = bot.get_move()