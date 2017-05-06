import random
from collections import defaultdict

class RPSEngine(object):
    RPS = {
        "R" : "P",
        "P" : "S",
        "S" : "R",
    }

    def __init__(self):
        self.db = defaultdict(lambda: { "R" : 0, "P" : 0, "S" : 0 })
        self.state = []

    def learn(self, inp):
        if(len(self.state) == 5):
            self.db[tuple(self.state)][inp] += 1
            del self.state[0]
        self.state.append(inp)

    def decide(self):
        if(len(self.state) == 5):
            possible = sorted(self.db[tuple(state)].iteritems(), key=lambda i: i[1])
            if possible[0][1] == 0:
                return random.choice(self.RPS.keys())
            else:
                return self.RPS[possible[0][0]]
        else:
            return random.choice(self.RPS.keys())

rpsengine = RPSEngine()
rpsengine.learn(input)
output = rpsengine.decide()