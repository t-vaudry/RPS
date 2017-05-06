if input == "":

    import collections
    import random
    import math

    gamma = random.gammavariate
    sqrt = math.sqrt
    log =math.log
    R, P, S = 0, 1, 2
    index = {"R": R, "P": P, "S": S}
    beat = (P, S, R)
    name = ("R", "P", "S")
    strategies = [("P", "S", "R"),
                  ("S", "R", "P"),
                  ("R", "P", "S")]

    history = collections.deque([])

    def ucb(s, n, t):
        return (s / n) + sqrt(2 * log(t) / n)

    def random_index(ps):
        t = sum(ps)
        r = random.uniform(0, t)
        x = 0
        for i, p in enumerate(ps):
            x += p
            if r <= x:
                break
        return i

    class MixTree:
        def __init__(self):
            self.counts = [0 for _ in xrange(3)]
            self.children = None

        def update(self, h, i, prediction=None):
            stop = False
            for d, k in enumerate(h):
                self.counts[i] += 2
                if stop or d >= 16:
                    return
                if self.children is None:
                    self.children = [None for _ in xrange(3)]
                if self.children[k] is None:
                    self.children[k] = MixTree()
                    stop = True
                self = self.children[k]

        def predict(self, h):
            n0 = [1, 1, 1]
            for d, k in enumerate(h):
                for i, x in enumerate(self.counts):
                    n0[i] += x
                if self.children is None:
                    break
                child = self.children[k]
                if child is None:
                    break
                self = child
            return n0

    class SwitchTree:
        def __init__(self, counts = None):
            self.counts = [0.0 for _ in xrange(3)]
            self.visits = [0.0 for _ in xrange(3)]
            self.children = None

        def score(self, t):
            return ucb(self.pos_total, self.neg_total, self.total_visits, t)

        def select_move(self, t):
            n = sum(self.counts)
            m = sum(1 for x in self.counts if x)
            if m == 0:
                a = 0.5
            else:
                a = m / (6 * log((n + 1.0) / m))
            r = gamma(self.counts[0] + a, 1)
            p = gamma(self.counts[1] + a, 1)
            s = gamma(self.counts[2] + a, 1)
            scores = [s - p, r - s, p - r]
            scores = [ucb(s, n + 0.5, t) for s, n in zip(scores, self.visits)]
            best = max(scores)
            return (best, scores.index(best))

        def update(self, h, i):
            for n in h:
                self.counts[i] += 1
                if self.children is None:
                    break
                self = self.children[n]
                if self is None:
                    break

        def predict(self, h):
            path = []
            stop = False
            path.append(self)
            for d, n in enumerate(h):
                if stop or d >= 16:
                    break
                if self.children is None:
                    self.children = [None for _ in xrange(3)]
                if self.children[n] is None:
                    self.children[n] = SwitchTree()
                    stop = True
                child = self.children[n]
                self = child
                path.append(self)
            t = sum(1.5 + sum(node.visits) for node in path)
            best_score = float("-inf")
            for i, n in enumerate(path):
                score, move = n.select_move(t)
                if score >= best_score:
                    j = i
                    best_score = score
                    best_node = n
                    best_move = move
            return (best_node, best_move)
    mix = MixTree()
    switch = SwitchTree()
    node = switch
    scores = [[0, 0], [0, 0]]
    visits = [0, 0]
else:

    i = index[input]
    j = index[output]
    for k, p in enumerate([p0, p1]):
        if p == beat[i]:
            scores[k][0] += 1
        elif i == beat[p]:
            scores[k][1] += 1
    mix.update(history, i)
    node.visits[j] += 1
    switch.update(history, i)
    history.appendleft(i)
    history.appendleft(j)

counts = mix.predict(history)
hypotheses = [random_index(counts) for _ in xrange(6)]
es = [0, 0, 0]
for i, _ in enumerate(es):
    for h in hypotheses:
        if i == beat[h]:
            es[i] += 1
        elif h == beat[i]:
            es[i] -= 1
best = max(es)
p0 = random.choice([i for i in xrange(3) if es[i] == best])
node, p1 = switch.predict(history)
s0 = (scores[0][0] - scores[0][1]) / (sum(scores[0]) + 1.0)
s1 = (scores[1][0] - scores[1][1]) / (sum(scores[1]) + 1.0)
t = sum(visits)
m = 2 * log(t + 1.0)
if s0 + sqrt(m / (visits[0] + 1.0)) > s1 + sqrt(m / (visits[1] + 1.0)):
    p = p0
    visits[0] += 1
else:
    p = p1
    visits[1] += 1
output = name[p]