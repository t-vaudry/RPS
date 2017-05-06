if input == "":

    import math
    log = math.log
    exp = math.exp
    log_half = log(0.5)
    third = 1.0 / 3.0
    log_third = log(1.0/3.0)
    log_fourth = log(1.0/4.0)
    log_two_thirds = log(2.0/3.0)

    def log_add(x, y):
        if y > x:
            x, y = y, x
        d = y - x
        if d < -60:
            return x
        return x + log(1.0 + exp(d))

    class Blender:
        def __init__(self, models):
            self.log_ps = [0 for _ in xrange(models)]
        def update(self, cond_probs):
            for k, p in enumerate(cond_probs):
                self.log_ps[k] += log(p)
        def predict(self, cond_probss):
            log_ps = [float("-inf") for _ in cond_probss[0]]
            for model, cond_probs in enumerate(cond_probss):
                for i, p in enumerate(cond_probs):
                    log_ps[i] = log_add(log_ps[i], self.log_ps[model] + log(p))
            log_p0 = min(log_ps)
            ps = [exp(log_p - log_p0) for log_p in log_ps]
            rt = 1.0 / sum(ps)
            for i, p in enumerate(ps):
                ps[i] *= rt
            return ps

    class ContextTree:
        def __init__(self):
            self.counts = [0, 0, 0]
            self.children = [None, None, None]
        def path(self, history):
            nodes = []
            i   = 0
            end = min(len(history) - 1, 32)
            while True:
                nodes.append(self)
                if i >= end:
                    break
                x = history[i]
                child = self.children[x]
                if child is None:
                    child = ContextTree()
                    self.children[x] = child
                    nodes.append(child)
                    break
                i += 1
                self = child
            return nodes

    def update(path, c):
        i = len(path) - 1
        while i >= 0:
            node = path[i]
            b = node.counts[c] == 0
            node.counts[c] += 1
            if not b:
                return
            i -= 1

    def predict(path):
        counts = [0, 0, 0]
        for node in path:
            for i, n in enumerate(node.counts):
                counts[i] += n
        return counts

    import collections
    import random
    import math
    log = math.log

    R, P, S = range(3)
    index = {"R": R, "P": P, "S": S}
    name = ("R", "P", "S")
    beat   = (P, S, R)
    beaten = (S, R, P)
    model = ContextTree()
    blender = Blender(3)
    history = collections.deque([])
    output = random.choice(name)
    ps = [1.0 / 3.0 for _ in xrange(3)]
else:
    i = index[input]
    blender.update((ps[(i + k) % 3] for k in xrange(3)))
    j = index[output]
    nodes = model.path(history)
    history.appendleft(j)
    history.appendleft(i)
    update(nodes, i)
    counts = [n + 1 for n in predict(nodes)]
    t = sum(counts)
    rt = 1.0 / t
    ps = [n * rt for n in counts]
    beta = t * t + 1.0
    alpha = beta / 3.0
    for i, n in enumerate(counts):
        counts[i] = random.gammavariate(n + alpha, 1)
    rt = 1.0 / sum(counts)
    qs = [n * rt for n in counts]
    qss = [[qs[(l + k) % 3] for l in xrange(3)] for k in xrange(3)]
    rs = blender.predict(qss)
    scores = [0, 0, 0]
    for k, n in enumerate(rs):
        scores[beat[k]]   += n
        scores[beaten[k]] -= n
    output = name[scores.index(max(scores))]