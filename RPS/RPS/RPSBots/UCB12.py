if input == "":

    import collections
    import math
    import random

    gamma = random.gammavariate
    sqrt = math.sqrt
    log = math.log
    R, P, S = 0, 1, 2
    index = {"R": R, "P": P, "S": S}
    beat = (P, S, R)
    beaten = (S, R, P)
    name = ("R", "P", "S")

    def ucb(s, n, t):
        return s + sqrt(2 * log(t) / n)

    class MarkovTree:
        def __init__(self, parent = None):
            self.counts = [1.0 for _ in xrange(3)]
            self.visits = [1.0 for _ in xrange(3)]
            self.children = None
            self.parent = parent

        def select_move(self, t):
            counts = self.counts
            scores = [0, 0, 0]
            for j in xrange(3):
                n0 = gamma(counts[beaten[j]], 1)
                n1 = gamma(counts[beat[j]], 1)
                n2 = gamma(counts[j], 1)
                s = (n0 - n1) / (n0 + n1 + n2)
                scores[j] = ucb(s, self.visits[j], t)
            best = max(scores)
            return (best, scores.index(best))

        def update(self, h, i):
            for n in h:
                self.counts[i] += 1
                if self.children is None:
                    self.children = [None for _ in xrange(3)]
                if self.children[n] is None:
                    self.children[n] = MarkovTree()
                    break;
                self = self.children[n]

        def predict(self, h):
            t = sum(self.visits)
            path = [self]
            for d, n in enumerate(h):
                if d >= 16:
                    break
                if self.children is None:
                    break;
                if self.children[n] is None:
                    break;
                self = self.children[n]
                t += sum(self.visits)
                path.append(self)
            best_score = 0
            chosen = self
            best_move = random.choice((R, P, S))
            for node in path:
                score, move = node.select_move(t)
                if score >= best_score:
                    best_score = score
                    best_move = move
                    chosen = node
            for node in path:
                node.visits[best_move] += 1
            return (chosen, best_move)

    tree = MarkovTree()
    history = collections.deque([])

else:

    i = index[input]
    j = index[output]

    tree.update(history, i)

    history.appendleft(i)
    history.appendleft(j)

node, m = tree.predict(history)
output = name[m]