if input == "":

    import collections
    import math
    import random

    unit_random = random.random
    log = math.log
    exp = math.exp

    def log_add(a, b):
        if a > b:
            a, b = b, a
        d = b - a
        return log(1 + exp(d)) + a if d <= 50.0 else b

    def weighted_sample(counts, t):
        r = random.uniform(0, t)
        for i, n in enumerate(counts):
            r -= n
            if r <= 0:
                break
        return i

    log_half = log(0.5)

    class CTWNode:
        def __init__(self):
            self.counts = [1.0, 1.0, 1.0]
            self.total = 3.0
            self.log_p = 0.0
            self.log_p_self = 0.0
            self.log_p_children = 0.0
            self.children = None
        def update(self, context, depth, symbol):
            n = self.counts[symbol] 
            self.log_p_self += log(n / self.total)
            self.counts[symbol] += 1.0
            self.total += 1.0
            if depth >= min(16, len(context)):
                return self.log_p_self
            if self.children is None:
                self.children = [None, None, None]
            child = self.children[context[depth]]
            if child is None:
                child = CTWNode()
                self.children[context[depth]] = child
            self.log_p_children -= child.log_p
            child.update(context, depth + 1, symbol)
            self.log_p_children += child.log_p
            self.log_p = log_add(self.log_p_self, self.log_p_children) + log_half
        def sample(self, context):
            depth = 0
            while True:
                if self.children is None:
                    break
                p_halt = self.log_p_self - log_add(self.log_p_self, self.log_p_children)
                if unit_random() <= p_halt:
                    break
                child = self.children[context[depth]]
                if child is None:
                    break
                self = child
                depth += 1
            return weighted_sample(self.counts, self.total)

    R, P, S = range(3)
    index = {"R": R, "P": P, "S": S}
    name = ("R", "P", "S")
    beat = (P, S, R)
    beaten = (S, R, P)
    model = CTWNode()
    context = collections.deque([])

else:
    u = index[input]
    v = index[output]

    model.update(context, 0, u)

    context.appendleft(u)
    context.appendleft(v)

scores = [0,0,0]

for _ in xrange(3):
    s = model.sample(context)
    scores[beat[s]] += 1
    scores[beaten[s]] -= 1

m = max(scores)
output = name[random.choice([k for k, x in enumerate(scores) if x == m])]