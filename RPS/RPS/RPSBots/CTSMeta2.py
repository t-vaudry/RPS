if input == "":
    import math
    log = math.log
    exp = math.exp
    log_half = log(0.5)
    third = 1.0 / 3.0
    log_third = log(1.0/3.0)
    log_two_thirds = log(2.0/3.0)

    def log_add(x, y):
        if y > x:
            x, y = y, x
        d = y - x
        if d < -60:
            return x
        return x + log(1.0 + exp(d))

    def log_sub(x, y):
        d = y - x
        return x + log(1.0 - exp(d))

    def log_mean(x, y):
        return log_half + log_add(x, y)

    def log_mean_3(x, y, z):
        return log_third + log_add(log_add(x, y), z)

    def meta(k, c):
        if k == c:
            d = 0
        elif k == beat[c]:
            d = 1
        else:
            d = 2
        return d

    class ContextTree:
        def __init__(self):
            self.p = 0.0
            self.p_children = 0.0
            self.weights = [log_third for _ in xrange(3)]
            self.counts = [0, 0, 0]
            self.meta_counts = [0, 0, 0]
            self.children = [None, None, None]
        def update(self, alpha, beta, history, c, i=0):
            counts = self.counts
            meta_counts = self.meta_counts
            scores = [0.0 for _ in xrange(3)]
            for j in xrange(3):
                scores[j] = counts[beaten[j]] - counts[beat[j]]
            k = scores.index(max(scores))
            d = meta(k, c)
            rt = 1.0 / (sum(counts) + 1.0)
            cond_p_self = log((counts[c] + third) * rt)
            cond_p_meta = log((meta_counts[d] + third) * rt)
            counts[c] += 1
            meta_counts[d] += 1
            if i >= min(len(history) - 1, 10):
                self.p += cond_p_self
                return
            x = history[i]
            if self.children[x] is None:
                self.children[x] = ContextTree()
            self.children[x].update(alpha, beta, history, c, i + 1)
            p_children = 0.0
            for child in self.children:
                if child is not None:
                    p_children += child.p
            w0, w1, w2 = self.weights
            cond_p_children = p_children - self.p_children
            self.p_children = p_children
            self.p = log_add(log_add(w0 + cond_p_self, w1 + cond_p_meta), w2 + cond_p_children)
            probs = (cond_p_self, cond_p_meta, cond_p_children)
            base = alpha + self.p
            for i, (w, p) in enumerate(zip(self.weights, probs)):
                self.weights[i] = log_add(base, beta + w + p)
        def predict(self, history, ps, i=0):
            counts = self.counts
            meta_counts = self.meta_counts
            scores = [0.0 for _ in xrange(3)]
            for j in xrange(3):
                scores[j] = counts[beaten[j]] - counts[beat[j]]
            k = scores.index(max(scores))
            rt = 1.0 / (sum(counts) + 1.0)
            cond_p_self = (log((counts[c] + third) * rt) for c in xrange(3))
            cond_p_meta = (log((meta_counts[meta(k, c)] + third) * rt) for c in xrange(3))
            if i >= min(len(history) - 1, 10):
                for i, p0 in enumerate(cond_p_self):
                    ps[i] += p0 + self.p
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
                elif y == x:
                    factor += log_third
            w0, w1, w2 = self.weights
            w3 = w2 + factor - self.p_children
            for i, (pse, pm, pc) in enumerate(zip(cond_p_self, cond_p_meta, p_children)):
                ps[i] += log_add(w0 + pse, log_add(w1 + pm, w3 + pc))

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
    rnd = 0
else:
    rnd += 1
    i = index[input]
    j = index[output]
    alpha = 1.0 / (rnd + 2)
    beta  = 1 - 2 * alpha
    model.update(log(alpha), log(beta), history, i)
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