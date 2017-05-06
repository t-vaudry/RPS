if input == "":

    import array
    import math
    import collections
    import random

    log = math.log
    exp = math.exp
    log_half = log(0.5)
    log_third = log(1/3.0)
    log_sixth = log(1/6.0)
    log2 = log(2.0)
    log3 = log(3.0)
    log5 = log(5.0)
    log7 = log(7.0)
    R, P, S = 0, 1, 2

    index = {"R": 0, "P": 1, "S": 2}
    name = ("R", "P", "S")
    beat = (1, 2, 0)


    def log_add(x, y):
        if y > x:
            x, y = y, x
        d = y - x
        if d < -60:
            return x
        return x + log(1.0 + exp(d))

    def laplace_smoothing(counts, i, x, n):
        if i == 0:
            used = 6
        else:
            used = 3
        return log(counts[x] + 1.0) - log(n + used)

    def meta_index(counts, i, x):
        n = counts[x]
        if x >= 3:
            o = 3
        else:
            o = 0
        expectations = [counts[o + R] - counts[o + S],
                        counts[o + P] - counts[o + R],
                        counts[o + S] - counts[o + P]]
        m = max(expectations)
        y = random.choice([i for i, y in enumerate(expectations) if y == m])
        x -= o
        if y == x:
            return o
        if y == beat[x]:
            return o + 2
        return o + 1

    class ContextTree:
        def __init__(self, n):
            self.log_p_kt = 0.0
            self.log_p_kt_meta = 0.0
            self.log_p = 0.0
            self.log_p_meta = 0.0
            self.counts = array.array('i',(0 for _ in xrange(n)))
            self.meta_counts = array.array('i',(0 for _ in xrange(n)))
            self.total = 0
            self.children = None
        def update(self, history, i=0):
            x = history[i]
            if i and (x >= 3):
                x -= 3
            self.log_p_kt += laplace_smoothing(self.counts, i, x, self.total)
            y = meta_index(self.counts, i, x)
            self.log_p_kt_meta += laplace_smoothing(self.meta_counts, i, y, self.total)
            self.counts[x] += 1
            self.meta_counts[y] += 1
            self.total += 1
            if self.total == 1 or i >= len(history) - 1 or i >= 32:
                self.log_p = self.log_p_kt
                self.log_p_meta = self.log_p_kt_meta
                return
            if self.children is None:
                self.children = [None for _ in xrange(len(self.counts))]
            if self.children[x] is None:
                self.children[x] = ContextTree(3)
            self.children[x].update(history, i + 1)
            log_p_children = 0
            log_p_children_meta = 0
            for child in self.children:
                if child is not None:
                    log_p_children += child.log_p
                    log_p_children_meta += child.log_p_meta
            self.log_p = log_add(self.log_p_kt, log_p_children) + log_half
            self.log_p_meta = log_add(self.log_p_kt_meta,
                                      log_p_children_meta) + log_half
        def predict(self, history, i=0):
            x = history[i]
            if i and x >= 3:
                x -= 3
            log_p_kt = self.log_p_kt + laplace_smoothing(self.counts, i, x, self.total)
            y = meta_index(self.counts, i, x)
            log_p_kt_meta = self.log_p_kt_meta + \
                            laplace_smoothing(self.meta_counts, i, y, self.total)
            if self.total == 0 or i >= len(history) - 1 or i >= 32:
                return (log_p_kt, log_p_kt_meta)
            log_p_children = 0
            log_p_children_meta = 0
            if self.children is not None:
                for y, child in enumerate(self.children):
                    if child is not None:
                        if y == x:
                            (a, b) = child.predict(history, i + 1)
                            log_p_children += a
                            log_p_children_meta += b
                        else:
                            log_p_children += child.log_p
                            log_p_children_meta += child.log_p_meta
                    elif y == x:
                        if i == 0:
                            log_p_children += log_sixth
                            log_p_children_meta += log_sixth
                        else:
                            log_p_children += log_third
                            log_p_children_meta += log_third
            return (log_add(log_p_kt, log_p_children) + log_half,
                    log_add(log_p_kt_meta, log_p_children_meta) + log_half)
    both = ContextTree(6)
    history = collections.deque([])
    output = random.choice(name)
else:
    i = index[input]
    j = index[output]
    history.appendleft(i)
    both.update(history)
    history.appendleft(3 + j)
    both.update(history)
    ps = [0.0, 0.0, 0.0]
    for i1, _ in enumerate(ps):
        history.appendleft(i1)
        (a, b) = both.predict(history)
        a = log_add(a, b) - log2
        ps[i1] = a
        history.popleft()
    t = log_add(log_add(ps[0], ps[1]), ps[2])
    scores = [0, 0, 0]
    for _ in xrange(3):
        r = t + log(random.random())
        for k, log_p in enumerate(ps):
            if k == 0:
                x = log_p
            else:
                x = log_add(x, log_p)
            if r <= x:
                break
        a = beat[k]
        b = beat[a]
        scores[a] += 1
        scores[b] -= 1
    m = max(scores)
    output = name[random.choice([k for k, x in enumerate(scores) if x == m])]