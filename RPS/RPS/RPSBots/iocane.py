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

    class MarkovPredictor:
        def __init__(self):
            self.seen = None
            self.children = None
        def update(self, h):
            s = h[-1]
            i = len(h) - 2
            d = 0
            while 0 <= i and d < 10:
                self.seen = s
                if self.children is None:
                    self.children = tuple(MarkovPredictor() for _ in range(3))
                self = self.children[h[i]]
                i -= 1
                d += 1
        def predict(self, h):
            i = len(h) - 1
            seen = R
            while self.seen is not None:
                seen = self.seen
                self = self.children[h[i]]
                i -= 1
            return seen

    class FrequencyPredictor:
        def __init__(self):
            self.frequencies = [0, 0, 0]
        def update(self, h):
            self.frequencies[h[-1]] += 1
        def predict(self, h):
            f = self.frequencies
            scores = [f[bad_against[m]] - f[good_against[m]] for m in moves]
            s = max(scores)
            return random.choice([m for m in moves if scores[m] == s])

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
                belief = [random.gammavariate(n + 0.5, 1) for n in counts]
                score = (belief[2] - belief[0]) / sum(belief)
                yield ((self.prediction + i) % 3, score)

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

    p0 = MetaPredictor(MarkovPredictor())
    p1 = MetaPredictor(FrequencyPredictor())
    p2 = RandomPredictor()
    model = PredictionBlender([p0, p1, p2])
    history = []
    output = random.choice(name)
else:
    us = index[output]
    them = index[input] 
    history.append(them)
    model.update(history)
    history.append(us)
    output = name[model.predict(history)]