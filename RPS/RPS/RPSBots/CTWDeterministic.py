if input == "":

    import array
    import math
    import random
    log = math.log
    exp = math.exp
    gamma = random.gammavariate
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
            used = 6
        else:
            used = 3
        n = sum(counts)
        return log(counts[x] + 1) - log(n + used)

    def laplace_smoothing(counts, i, x):
        if i == 0:
            used = 6
        else:
            used = 3
        n = sum(counts)
        return log(counts[x] + 1) - log(n + used)

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
            self.log_p_kt += laplace_smoothing(self.counts, i, x)
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
            log_p_kt = self.log_p_kt + laplace_smoothing(self.counts, i, x)
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
    history.appendleft(j + 3)
    model.update(history)
    ps = [0.0, 0.0, 0.0]
    for i1, _ in enumerate(ps):
        history.appendleft(i1)
        ps[i1] = model.predict(history)
        history.popleft()
    [r, p, s] = ps
    scores = [s - p, r - s, p - r]
    output = name[scores.index(max(scores))]