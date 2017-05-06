if input == "":

    import array
    import math
    log = math.log
    exp = math.exp
    log_half = log(0.5)
    log_third = log(1/3.0)
    log_sixth = log(1/6.0)
    log3 = log(3.0)

    def log_add(x, y):
        if y > x:
            x, y = y, x
        d = y - x
        if d < -60:
            return x
        return x + log(1.0 + exp(d))

    def laplace_smoothing(counts, i, x):
        if i == 0:
            used = 3
        else:
            used = 6
        n = sum(counts)
        return log(counts[x] + 1.0) - log(n + used)

    def meta_index(counts, i, x):
        n = counts[x]
        if i == 0:
            if x >= 3:
                counts = counts[3:]
                o = 3
            else:
                counts = counts[:3]
                o = 0
        else:
            counts = counts
            o = 0
        if n == max(counts):
            return o
        if n == min(counts):
            return o + 2
        return o + 1

    class ContextTree:
        def __init__(self, n=6):
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
            self.log_p_kt += laplace_smoothing(self.counts, i, x)
            y = meta_index(self.counts, i, x)
            self.log_p_kt_meta += laplace_smoothing(self.meta_counts, i, y)
            self.counts[x] += 1
            self.meta_counts[y] += 1
            self.total += 1
            if self.total == 1 or i >= len(history) - 1 or i >= 16:
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
            log_p_kt = self.log_p_kt + laplace_smoothing(self.counts, i, x)
            y = meta_index(self.counts, i, x)
            log_p_kt_meta = self.log_p_kt_meta + laplace_smoothing(self.meta_counts, i, y)
            if self.total == 0 or i >= len(history) - 1 or i >= 16:
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

    import collections
    import random
    index = {"R": 0, "P": 1, "S": 2}
    name = ("R", "P", "S")
    beat = (1, 2, 0)
    model = ContextTree()
    history = collections.deque([])
    output = random.choice(name)
else:
    i = index[input]
    j = index[output]
    history.appendleft(i)
    model.update(history)
    history.appendleft(j)
    model.update(history)
    ps = [0.0, 0.0, 0.0]
    uniform_iid_log_p = -(len(history) +  1) * log3
    for i1, _ in enumerate(ps):
        history.appendleft(i1)
        (a, b) = model.predict(history)
        a = log_add(a, b)
        a = log_add(a, uniform_iid_log_p)
        ps[i1] = a
        history.popleft()
    scores = [0, 0, 0]
    t = ps[0]
    t = log_add(t, ps[1])
    t = log_add(t, ps[2])
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