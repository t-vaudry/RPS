if input == "":

    import collections
    import random

    class MarkovTree:
        def __init__(self, counts = None):
            self.counts = [0 for _ in xrange(3)]
            self.children = None
            self.visits = 0

        def update(self, h, i):
            stop = False
            for d, k in enumerate(h):
                self.counts[i] += 2
                self.visits += 1
                if stop:
                    return
                if self.children is None:
                    self.children = [None for _ in xrange(3)]
                if self.children[k] is None:
                    self.children[k] = MarkovTree()
                    stop = True
                if self.visits < 9:
                    stop = True
                self = self.children[k]

        def predict(self, h, n0 = None):
            if n0 is None:
                n0 = [0, 0, 0]
            for d, k in enumerate(h):
                for i, x in enumerate(self.counts):
                    n0[i] += x
                if self.children is None:
                    break
                child = self.children[k]
                if child is None:
                    break
                self = child
            return n0

    R, P, S = 0, 1, 2
    index = {"R": R, "P": P, "S": S}
    beat = ("P", "S", "R")

    us = MarkovTree()
    them = MarkovTree()
    both = MarkovTree()

    us_history = collections.deque([])
    them_history = collections.deque([])
    both_history = collections.deque([])

else:

    i = index[input]
    j = index[output]
    
    us.update(us_history, i)
    them.update(them_history, i)
    both.update(both_history, i)

    us_history.appendleft(j)
    them_history.appendleft(i)
    both_history.appendleft(i)
    both_history.appendleft(j)

counts = us.predict(us_history)
them.predict(them_history, counts)
both.predict(both_history, counts)
ps = [random.gammavariate(n + 1, 1) for n in counts]
t = sum(ps)
r = random.uniform(0, t)
x = 0
for i, p in enumerate(counts):
    x += p
    if r <= x:
        break
output = beat[i]