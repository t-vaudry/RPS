import random

class MarkovChain:
    def __init__(self, counts = None):
        self.visits = 0
        if counts is None:
            self.counts = [1, 1, 1]
        else:
            self.counts = counts
        self.children = [self, self, self]

    def split_edge(self, i):
        old = self.children[i]
        new = MarkovChain(old.counts)
        self.children[i] = new
        for i in xrange(3):
            new.children[i] = old.children[i]

    def unnormalized_probabilities(self):
        return [x + 1 for x in self.counts]

    def transition(self, i):
        self.visits += 1
        self.counts[i] += 2
        child = self.children[i]
        if self.children[i].visits >= 2:
            self.split_edge(i)
        return self.children[i]

index = {"R": 0,
         "P": 1,
         "S": 2}

beat = {0: "P",
        1: "S",
        2: "R"}

if input == "":
   r0 = MarkovChain()
   g0 = MarkovChain()
   b0 = MarkovChain()
   r1 = MarkovChain()
   g1 = MarkovChain()
   b1 = MarkovChain()
   r2 = MarkovChain()
   g2 = MarkovChain()
   b2 = MarkovChain()
   children0 = [r0, g0, b0]
   children1 = [r1, g1, b1]
   children2 = [r2, g2, b2]
   for c in children0:
       c.children = children1
   for c in children1:
       c.children = children2
   for c in children2:
       c.children = children0
   model = MarkovChain()
   model.children = children0
else:
    i = index[input]
    j = index[output]
    model = model.transition(i)
    model = model.transition(j)
probs = model.unnormalized_probabilities()
t = sum(probs)
r = random.randrange(0, t)
x = 0
output = random.choice(["R", "P", "S"])
for i, p in enumerate(probs):
    x += p
    if r <= x:
        output = beat[i]
        break