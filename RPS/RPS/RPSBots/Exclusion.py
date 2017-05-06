if input == "":

    class ContextTree:
        def __init__(self):
            self.p_self = 0.0
            self.p = 0.0
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
        counts = [1, 1, 1]
        for node in path:
            for i, n in enumerate(node.counts):
                counts[i] += 1
        rt = 1.0 / sum(counts)
        for i, n in enumerate(counts):
            counts[i] *= rt
        return counts

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
    i = index[input]
    j = index[output]
    nodes = model.path(history)
    update(nodes, i)
    ps = predict(nodes)
    scores = [0, 0, 0]
    for _ in xrange(3):
        x = 0
        r = random.random()
        for k, p in enumerate(ps):
            x += p
            if x >= r:
                break
        scores[beat[k]]   += 1
        scores[beaten[k]] -= 1
    m = max(scores)
    output = name[random.choice([k for k, x in enumerate(scores) if x == m])]