if input == "":
    import math
    log = math.log
    exp = math.exp
    log_half = log(0.5)
    third = 1.0 / 3.0
    log_third = log(1.0/3.0)
    log_fourth = log(1.0/4.0)
    log_sixth = log(1.0/6.0)
    log_two_thirds = log(2.0/3.0)

    def log_add(x, y):
        if y > x:
            x, y = y, x
        d = y - x
        if d < -60:
            return x
        return x + log(1.0 + exp(d))

    def log_mean(x, y):
        return log_half + log_add(x, y)

    class ContextTree:
        def __init__(self):
            self.p_self = 0.0
            self.p = 0.0
            self.counts = [0, 0, 0]
            self.children = [None, None, None]
        def update(self, history, c, i=0):
            t = sum(self.counts) + 3.0
            self.p_self += log((self.counts[c] + 1.0) / t)
            self.counts[c] += 1
            if i >= len(history) - 1 or i >= 32:
                self.p = self.p_self
                return
            x = history[i]
            if self.children[x] is None:
                self.children[x] = ContextTree()
                self.children[x].counts[c] = 1.0
            else:
                self.children[x].update(history, c, i + 1)
            p_children = 0.0
            for child in self.children:
                if child is not None:
                    p_children += child.p
            self.p = log_add(self.p_self, p_children) + log_sixth
        def predict(self, history, ps, i=0):
            t = sum(self.counts) + 3.0
            p_self = (self.p_self + log((self.counts[c] + 1.0) / t) for c in xrange(3))
            if i >= len(history) - 1 or i >= 32:
                for i, p in enumerate(p_self):
                    ps[i] += p
                return
            x = history[i]
            p_children = [0.0 for _ in self.children]
            factor = 0.0
            for y, child in enumerate(self.children):
                if child is not None:
                    if y == x:
                        child.predict(history, p_children, i + 1)
                    else:
                        factor += child.p
            for j, p in enumerate(p_children):
                p_children[j] = p + factor
            p_below = (log_add(ps, pc) + log_sixth for ps, pc in zip(p_self, p_children))
            for i, p in enumerate(p_below):
                ps[i] += p

    import collections
    import random

    R, P, S = range(3)
    index = {"R": R, "P": P, "S": S}
    name = ("R", "P", "S")
    beat   = (P, S, R)
    beaten = (S, R, P)
    model = ContextTree()
    history = collections.deque([])
    output = random.choice(name)
else:
    d = 0
    i = index[input]
    print(i)
    j = index[output]
    model.update(history, i)
    history.appendleft(i)
    history.appendleft(j)
    ps = [0.0, 0.0, 0.0]
    model.predict(history, ps)
    p0 = min(ps)
    for i, p in enumerate(ps):
        ps[i] = exp(p - p0)
    scores = [0, 0, 0]
    t = sum(ps)
    for _ in xrange(3):
        x = 0
        r = random.uniform(0, t)
        for k, p in enumerate(ps):
            x += p
            if x >= r:
                break
        scores[beat[k]]   += 1
        scores[beaten[k]] -= 1
    m = max(scores)
    output = name[random.choice([k for k, x in enumerate(scores) if x == m])]