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

    def belief(counts):
        counts = [random.gammavariate(n + 0.5, 1) for n in counts]
        t = sum(counts)
        return [n / t for n in counts]

    class MarkovPredictor:
        def __init__(self):
            self.seen = None
            self.children = None
        def update(self, h):
            s = h[-1]
            i = len(h) - 2
            d = 0
            while d < 10:
                self.seen = s
                if self.children is None:
                    self.children = tuple(MarkovPredictor() for _ in range(3))
                if i < 0:
                    return
                self = self.children[h[i]]
                i -= 1
                d += 1
        def predict(self, h):
            i = len(h) - 1
            while self.seen is not None:
                seen = self.seen
                self = self.children[h[i]]
                i -= 1
            return seen

    class FrequencyPredictor:
        def __init__(self, k=1):
            self.k=k
            self.counts = [0, 0, 0]
        def update(self, h):
            self.counts[h[-1]] += 1
            for i, _ in enumerate(self.counts):
                self.counts[i] *= self.k
        def predict(self, h):
            p = belief(self.counts)
            scores = [p[bad_against[m]] - p[good_against[m]] for m in moves]
            return scores.index(max(scores))

    class MetaPredictor:
        def __init__(self, predictor):
            self.predictor = predictor    
            self.prediction = None
            self.counts = [[0 for _ in range(3)] for _ in range(3)]
        def update(self, h):
            s = h[-1]
            if self.prediction is not None:
                for i, counts in enumerate(self.counts):
                    m = (self.prediction + i) % 3
                    if m == good_against[s]:
                        counts[2] += 1
                    elif m == bad_against[s]:
                        counts[0] += 1
                    else:
                        counts[1] += 1
            self.predictor.update(h)
        def predictions(self, h):
            self.prediction = self.predictor.predict(h)
            for i, counts in enumerate(self.counts):
                p = belief(counts)
                yield ((self.prediction + i) % 3, p[2] - p[0])

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
            predictions = [p for predictor in self.predictors for p in predictor.predictions(h)] 
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
    output = random.choice(name)
else:
    us = index[output]
    them = index[input] 
    history.append(them)
    model.update(history)
    history.append(us)
    output = name[model.predict(history)]