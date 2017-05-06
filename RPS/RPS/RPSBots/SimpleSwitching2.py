if not input:

    import math
    import random
    import collections

    log = math.log
    exp = math.exp

    gamma = random.gammavariate

    third = 1.0 / 3

    thirds = [third for _ in xrange(3)]

    log_third = log(third)

    nmodels = 20
    models = range(nmodels)
    log_nmodels = log(nmodels)
    log_nmodelsm1 = log(nmodels - 1.0)
    log_weights = [-log_nmodels for _ in models]

    def log_add(x, y):
        if y > x:
            x, y = y, x
        d = y - x
        if d < -60:
            return x
        return x + log(1.0 + exp(d))

    class ContextTree:
        def __init__(self):
            self.counts = [0, 0, 0]
            self.children = [None, None, None]
        def update(self, history, input):
            l = len(history)
            i = 0
            while i < nmodels - 1:
                self.counts[input] += 1
                if i >= l:
                    return
                x = history[i]
                if self.children[x] is None:
                    self.children[x] = ContextTree()
                self = self.children[x]
                i += 1
        def path(self, history):
            l = len(history)
            i = 0
            while i < nmodels - 1:
                yield self.counts
                if i >= l:
                    return
                x = history[i]
                if self.children[x] is None:
                    return
                self = self.children[x]
                i += 1

    def cond_probs(path):
        yield thirds
        i = 0
        for counts in path:
            rt = 1.0 / (sum(counts) + 3.0)
            yield [(n + 1.0) * rt for n in counts]
            i += 1
        while i < nmodels - 1:
            yield thirds
            i += 1

    def sample_probs(path):
        yield thirds
        i = 0
        for counts in path:
            counts1 = [gamma(n + 1, 1) for n in counts]
            rt = 1.0 / (sum(counts1) + 3.0)
            yield [n * rt for n in counts1]
            i += 1
        while i < nmodels - 1:
            counts1 = [gamma(1, 1) for _ in names]
            rt = 1.0 / (sum(counts1) + 3.0)
            yield [n * rt for n in counts1]
            i += 1


    names = ["R", "P", "S"]
    R, P, S = range(3)
    index = dict(zip(names, range(3)))
    beat = (P, S, R)
    beaten = (S, R, P)

    model = ContextTree()
    history = collections.deque([])
    output = random.choice(names)

    cond_ps = [thirds for _ in models]

    rnd = 1.0

else:

    rnd += 1

    alpha = 1.0 / rnd

    k = (1 - alpha) * (nmodels - 1) - 1

    alpha = log(alpha)

    k = log(k)

    inp = index[input]
    out = index[output]

    log_inp_ps = [log(ps[inp]) for ps in cond_ps]

    r = float("-infinity")
    for w, p in zip(log_weights, log_inp_ps):
        r = log_add(r, w + p)

    for i, (w, p) in enumerate(zip(log_weights, log_inp_ps)):
        log_weights[i] = log_add(alpha + r, k + w + p) - log_nmodelsm1

    model.update(history, inp)

    history.appendleft(inp)
    history.appendleft(out)

    path = list(model.path(history))

    cond_ps = list(cond_probs(path))

    sampled_ps = list(sample_probs(path))

    log_cond_ps = [float("-infinity") for _ in names]

    for i, (w, ps) in enumerate(zip(log_weights, sampled_ps)):
        for j, p in enumerate(ps):
            log_cond_ps[j] = log_add(log_cond_ps[j], w + log(p))

    log_p0 = min(log_cond_ps)

    weighted_cond_ps = [0 for _ in names]

    for j, log_p in enumerate(log_cond_ps):
        weighted_cond_ps[j] = exp(log_p - log_p0)

    scores = [0, 0, 0]

    for i, p in enumerate(weighted_cond_ps):
        scores[beat[i]] += p
        scores[beaten[i]] -= p
    print(scores)
    output = names[scores.index(max(scores))]