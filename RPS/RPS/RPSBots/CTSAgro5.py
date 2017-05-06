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

    class CTSNode:
        def __init__(self):
            self.counts = [1.0, 1.0, 1.0]
            self.total = 3.0
            self.log_p = 0.0
            self.self_weight = log_half
            self.children_weight = log_half
            self.children = None

        def update(self, context, depth, symbol, log_alpha, log_beta):

            log_p_given_self = log(self.counts[symbol] / self.total)

            self.counts[symbol] += 1.0
            self.total += 1.0

            if depth >= min(14, len(context)):
                self.log_p += log_p_given_self
                return
            if self.children is None:
                self.children = [None, None, None]
            child = self.children[context[depth]]
            if child is None:
                child = CTSNode()
                self.children[context[depth]] = child

            log_p0 = child.log_p
            child.update(context, depth + 1, symbol, log_alpha, log_beta)
            log_p_given_children = child.log_p - log_p0

            k = self.self_weight
            s = self.children_weight

            self.log_p = log_add(k + log_p_given_self, s + log_p_given_children)

            p = log_alpha + self.log_p

            self.self_weight = log_add(p, log_beta + k + log_p_given_self)
            self.children_weight = log_add(p, log_beta + s + log_p_given_children)

        def sample(self, context):
            depth = 0
            while True:
                if self.children is None:
                    break
                log_p_halt = self.self_weight - log_add(self.self_weight, self.children_weight)
                if log(unit_random()) <= log_p_halt:
                    break
                child = self.children[context[depth]]
                if child is None:
                    break
                self = child
                depth += 1
            return weighted_sample(self.counts, self.total)

    def sample(models, contexts):
        t = models[0].log_p
        for m in models[1:]:
            t = log_add(t, m.log_p)
        log_ps = []
        for m in models:
            log_ps.append(m.log_p - t)
        ps = [exp(log_p) for log_p in log_ps]
        i = weighted_sample(ps, 1)
        return models[i].sample(contexts[i])

    R, P, S = range(3)
    index = {"R": R, "P": P, "S": S}
    name = ("R", "P", "S")
    beat = (P, S, R)
    beaten = (S, R, P)
    model = CTSNode()
    my_model = CTSNode()
    their_model = CTSNode()
    models = [model, my_model, their_model]
    context = collections.deque([])
    my_context = collections.deque([])
    their_context = collections.deque([])
    contexts = [context, my_context, their_context]
    rnd = 3

else:

    u = index[input]
    v = index[output]

    alpha = 1.0 / rnd
    beta = 1 - 2 * alpha
    log_alpha = log(alpha)
    log_beta = log(beta)
    rnd += 1

    model.update(context, 0, u, log_alpha, log_beta)
    my_model.update(my_context, 0, u, log_alpha, log_beta)
    their_model.update(their_context, 0, u, log_alpha, log_beta)

    context.appendleft(u)
    context.appendleft(v)

    my_context.appendleft(v)
    their_context.appendleft(u)

scores = [0,0,0]

for _ in range(rnd // 200 + 1):
    s = sample(models, contexts)
    scores[beat[s]] += 1
    scores[beaten[s]] -= 1
output = name[scores.index(max(scores))]