import collections
import random
import re

MOVES = 2


class MarkovChain:
    history = ""
    win = {"R": "P", "P": "S", "S": "R"}

    def learn(self, i):
        self.history += i

    def decide(self):
        p = []
        if len(self.history) < MOVES:
            return self.win[random.choice(["R", "P", "S"])]
        else:
            idx = [m.start()
                   for m in re.finditer(self.history[:-MOVES], self.history)]
            p = [self.history[i + MOVES] for i in idx]
            c = collections.Counter(p)
            return c.most_common[0][1]

m = MarkovChain()
m.learn(input)
output = m.decide()