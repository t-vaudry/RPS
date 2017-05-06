if input == "":

    import array
    import math
    log = math.log
    exp = math.exp
    log_half = log(0.5)
    log_third = log(1/3.0)
    log_sixth = log(1/6.0)
    sqrt = math.sqrt

    def log_add(x, y):
        if y > x:
            x, y = y, x
        d = y - x
        if d < -60:
            return x
        return x + log(1.0 + exp(d))

    def kt_smoothing(counts, i, x):
        m = float(sum(1 for x in counts if x != 0))
        n = sum(counts)
        if i == 0:
            used = 6
        else:
            used = 3
        return log(counts[x] + 0.5) - log(n + 0.5 * used)

    class ContextTree:
        def __init__(self, n=6):
            self.log_p_kt = 0.0
            self.log_p = 0.0
            self.counts = array.array('i',(0 for _ in xrange(n)))
            self.total = 0
            self.children = None
        def update(self, history, i=0):
            x = history[i]
            if i and (x >= 3):
                x -= 3
            self.log_p_kt += kt_smoothing(self.counts, i, x)
            self.total += 1
            self.counts[x] += 1
            if self.total == 1 or i >= len(history) - 1 or i >= 16:
                self.log_p = self.log_p_kt
                return
            if self.children is None:
                self.children = [None for _ in xrange(len(self.counts))]
            if self.children[x] is None:
                self.children[x] = ContextTree(3)
            self.children[x].update(history, i + 1)
            log_p_children = 0
            for child in self.children:
                if child is not None:
                    log_p_children += child.log_p
            self.log_p = log_add(self.log_p_kt, log_p_children) + log_half
        def predict(self, history, i=0):
            x = history[i]
            if i and (x >= 3):
                x -= 3
            log_p_kt = self.log_p_kt + kt_smoothing(self.counts, i, x)
            if self.total == 0 or i >= len(history) - 1 or i >= 16:
                return log_p_kt
            log_p_children = 0
            if self.children is not None:
                for y, child in enumerate(self.children):
                    if child is not None:
                        if y == x:
                            log_p_children += child.predict(history, i + 1)
                        else:
                            log_p_children += child.log_p
                    elif y == x:
                        if i == 0:
                            log_p_children += log_sixth
                        else:
                            log_p_children += log_third
            return log_add(log_p_kt, log_p_children) + log_half

    import collections
    import random
    index = {"R": 0, "P": 1, "S": 2}
    name = ("R", "P", "S")
    beat = (1, 2, 0)
    model = ContextTree()
    history = collections.deque([])
    output = random.choice(name)
    turn = 2
    beta0 = -log(2) / log(3)
else:
    beta = beta0 - 1 / turn
    turn += 1
    i = index[input]
    j = index[output]
    history.appendleft(i)
    model.update(history)
    history.appendleft(j + 3)
    model.update(history)
    log_p0 = [0.0, 0.0, 0.0]
    for i1 in xrange(3):
        history.appendleft(i1)
        log_p0[i1] = model.predict(history)
        history.popleft()
    t = log_p0[0]
    t = log_add(t, log_p0[1])
    t = log_add(t, log_p0[2])
    p0 = [exp(log_p - t) for log_p in log_p0]
    qs = [0 for _ in xrange(3)]
    for y in xrange(3):
        p = p0[y]
        for x in xrange(3):
            if x == beat[y]:
                s = 1
            elif y == beat[x]:
                s = -1
            else:
                s = 0
            qs[x] += p * s
    sr, sp, ss = qs
    ps = [exp(beta * q) for q in qs]
    p = 0
    r = random.uniform(0, sum(ps))
    for x in xrange(3):
        p += ps[x]
        if r <= p:
            break
    output = name[x]