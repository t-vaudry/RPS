from random import choice, uniform

class Counter(dict):
    def __getitem__(self, idx):
        self.setdefault(idx, 0)
        return dict.__getitem__(self, idx)

    def argMax(self):
        if len(self.keys()) == 0:
            return choice('RPS')

        all = self.items()
        values = [x[1] for x in all]
        maxIndex = values.index(max(values))

        return all[maxIndex][0]

class Strategy:
    def update(self, state):
        pass

    def getAction(self):
        pass

class RegexStrategy(Strategy):
    def __init__(self, depth):
        self.depth = depth

        self.history = []
        self.stateLocations = {}

    def update(self, state):
        self.stateLocations.setdefault(state, [])
        self.stateLocations[state].append(len(self.history))

        self.history.append(state)

    def getAction(self):
        if len(self.stateLocations[self.history[-1]]) == 1:
            return choice('RPS')

        actions = Counter()
        for index in self.stateLocations[self.history[-1]][:-1]:
            recent = -1
            action = self.history[index + 1][1]

            while index > -1 and recent >= -self.depth and \
                    self.history[index] == self.history[recent]:
                actions[action] += 1

                index -= 1
                recent -= 1
        return {'R': 'P',
                'P': 'S',
                'S': 'R'}[actions.argMax()]

class DiscountedStateStrategy(Strategy):
    def __init__(self, discount):
        self.discount = discount

        self.lastState = ('', '')
        self.history = {}

    def update(self, state):
        for _, counter in self.history.items():
            for key in counter.keys():
                counter[key] *= self.discount

        self.history.setdefault(self.lastState, Counter())
        self.history[self.lastState][state[1]] += 1

        self.lastState = state

    def getAction(self):
        self.history.setdefault(self.lastState, Counter())
        return {'R': 'P',
                'P': 'S',
                'S': 'R'}[self.history[self.lastState].argMax()]

def weightedChoice(choices):
    total = sum(w for c, w in choices)
    r = uniform(0, total)
    upto = 0
    for c, w in choices:
        if upto + w > r:
            return c
        upto += w

if input == '':
    strategies = [(DiscountedStateStrategy(.50), .50),
                  (RegexStrategy(1),             .50)]
    output = choice('RPS')
else:
    for strategy, _ in strategies:
        strategy.update((output, input))
    output = weightedChoice(strategies).getAction()