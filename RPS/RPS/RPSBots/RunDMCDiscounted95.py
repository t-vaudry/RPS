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
        new.children = old.children

    def unnormalized_probabilities(self):
        return [n + 1 for n in self.counts]

    def transition(self, i):
        self.visits += 1
        self.counts[i] += 1
        for i in xrange(3):
            self.counts[i] *= 0.95
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
   p0 = MarkovChain()
   s0 = MarkovChain()
   r1 = MarkovChain()
   p1 = MarkovChain()
   s1 = MarkovChain()
   r2 = MarkovChain()
   p2 = MarkovChain()
   s2 = MarkovChain()
   children0 = [r0, p0, s0]
   children1 = [r1, p1, s1]
   children2 = [r2, p2, s2]
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
r = random.uniform(0, t)
x = 0
for i, p in enumerate(probs):
    x += p
    if r <= x:
        output = beat[i]
        break