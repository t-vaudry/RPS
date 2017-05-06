if input == "":

    import collections
    import math
    import random

    gamma = random.gammavariate
    sqrt = math.sqrt
    log = math.log
    moves = R, P, S = 0, 1, 2
    index = {"R": R, "P": P, "S": S}
    good_against = (P, S, R)
    bad_against = (S, R, P)
    name = ("R", "P", "S")
    ages = [1, 2, 4, 16, 64, 256, float('inf')]

    def belief(counts):
        counts = [random.gammavariate(n + 0.5, 1) for n in counts]
        t = sum(counts)
        return [n / t for n in counts]

    class MarkovPredictor:
        def __init__(self):
            self.length = 0
            self.seen = None
            self.children = None
        def update(self, h):
            s = h[-1]
            l = len(h)
            i = l - 2
            d = 0
            stop = False
            while d < 15:
                self.seen = s
                self.length = l
                if i < 0 or stop:
                    return
                if self.children is None:
                    self.children = [None]*3
                m = h[i]
                child = self.children[m]
                if child is None:
                    stop = True
                    child = self.children[m] = MarkovPredictor()
                self = child
                i -= 1
                d += 1
        def predictions(self, h):
            l = len(h)
            i = l - 1
            j = 0
            results = []
            seen = R
            while self is not None and self.seen is not None:
                if (l - self.length) > ages[j]:
                    j+=1
                    results.append(seen)
                seen = self.seen
                if self.children is None:
                    break
                self = self.children[h[i]]
                i -= 1
            while len(results) < len(ages):
                results.append(seen)
            return results

    class FrequencyPredictor:
        def __init__(self, k=1):
            self.k=k
            self.counts = [0, 0, 0]
        def update(self, h):
            self.counts[h[-1]] += 1
            for i, _ in enumerate(self.counts):
                self.counts[i] *= self.k
        def predictions(self, h):
            p = belief(self.counts)
            scores = [p[bad_against[m]] - p[good_against[m]] for m in moves]
            return [scores.index(max(scores))]

    class MetaPredictor:
        def __init__(self, predictor):
            self.predictor = predictor
            self.last_predictions = None
            self.counts = []
        def update(self, h):
            while len(self.counts) < len(self.last_predictions):
                self.counts.append([[0 for _ in range(3)] for _ in range(3)])
            s = h[-1]
            for p, n in zip(self.last_predictions, self.counts):
                for i, counts in enumerate(n):
                    m = (p + i) % 3
                    if m == good_against[s]:
                        counts[2] += 1
                    elif m == bad_against[s]:
                        counts[0] += 1
                    else:
                        counts[1] += 1
            self.predictor.update(h)
        def predictions(self, h):
            self.last_predictions = self.predictor.predictions(h)
            for m, n in zip(self.last_predictions, self.counts): 
                for i, counts in enumerate(n):
                    p = belief(counts)
                    pr = ((m + i) % 3, p[2] - p[0])
                    yield pr

    class RandomPredictor:
        def __init__(self):
            pass
        def update(self, h):
            pass
        def predictions(self, h):
            return [(random.choice(moves), 0)]

    class PredictionBlender:
        def __init__(self, predictors):
            self.predictors = predictors
        def update(self, h):
            for predictor in self.predictors:
                predictor.update(h)
        def predict(self, h):
            predictions = (p for predictor in self.predictors for p in predictor.predictions(h))
            best_score = float('-inf')
            for m, score in predictions:
                if score > best_score:
                    move = m
                    best_score = score
            return move

    predictors = [
        MetaPredictor(MarkovPredictor()),
        MetaPredictor(FrequencyPredictor()),
        MetaPredictor(FrequencyPredictor(k=0.99)),
        MetaPredictor(FrequencyPredictor(k=0.9)),
        MetaPredictor(FrequencyPredictor(k=0.8)),
        MetaPredictor(FrequencyPredictor(k=0.5)),
        RandomPredictor()
    ]
    model = PredictionBlender(predictors)
    history = []
else:
    us = index[output]
    them = index[input] 
    history.append(them)
    model.update(history)
    history.append(us)
output = name[model.predict(history)]