from collections import defaultdict
import random

MOVES = 'RPS'
#SYMBOLS = MOVES
SYMBOLS = [c1 + c2 for c1 in MOVES for c2 in MOVES]


class UnboundedNGramPredictor:
    def __init__(self, alpha=0.97):
        self.alpha = alpha
        self.log = defaultdict(float)
        for c in SYMBOLS:
            self.log[c] += 1

    def prob(self, c, history):
        if not history:
            return float(self.log[c]) / sum(self.log[s] for s in SYMBOLS)
        d = sum(self.log[history + s] for s in SYMBOLS)
        if d > 0.1:
            pred_c = float(self.log[history + c]) / d
            pred_p = self.prob(c, history[2:])
            return pred_c * (1.0 - self.alpha) + pred_p * self.alpha
        return self.prob(c, history[2:])

    def add_history(self, history):
        for i in range(2, len(history) + 1, 2):
            self.log[history[-i:]] += 1


if not input:
    predictor = UnboundedNGramPredictor()
    history = ''
    history_my = ''
    output = 'P'
    random.seed(123)
    last_loses = 0
    d = {'R': 'P', 'P': 'S', 'S': 'R'}
    translations = {'R': 'P', 'P': 'S', 'S': 'R'}
else:
    if history:
        if d[history[-1]] == history_my[-1]:
            last_loses -= 0.1
        elif d[history_my[-1]] == history[-1]:
            last_loses += 1
        if last_loses >= 10:
            translations_next = {}
            for c in translations:
                translations_next[c] = d[translations[c]]
            translations = translations_next
    history += input
    history = history[-10:]
    history_my = history_my[-10:]
    hh = ''.join(map(''.join, zip(history, history_my)))
    predictor.add_history(hh)
    r = random.random()
    for c in SYMBOLS:
        p = predictor.prob(c, hh)
        if p > r:
            output = translations[c[0]]
            history_my += output
            break
        r -= p