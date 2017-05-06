import random

# Helper stuff

BEATING_PLAYS = {"R":"P", "P":"S", "S":"R"}

# sample from a random distribution
def sample(dist):
    x = random.uniform(0, sum(dist.values()))
    for k, p in dist.iteritems():
        x -= p
        if x < 0:
            return k

# return the set of most-likely elements in a distribution
def modes(dist):
    m = max(dist.values())
    return [x for x, p in dist.iteritems() if p == m]

# a uniform distribution over the provided elements
def uniform_dist(elems):
    return dict((x, 1.0 / len(elems)) for x in elems)
    
# a non-random distribution
def singleton_dist(x):
    return uniform_dist([x])

# return the distribution of f(X) where X has distribution dist
def map_dist(dist, f):
    return dict((f(x), p) for x, p in dist.iteritems())
    

# A strategy is a function from history (represented as a list of (opponent_play, my_play) pairs, e.g. [("R", "S"), ("P", "R")])
# to a distribution over plays (represented as a dict mapping play to play_probability e.g. {"R": 0.5, "P": 0.25, "S": 0.25}).

# Given an opponent strategy, return the strategy that maximizes the probability of beating it.
def make_beater(opponent):
    def beater(history):
        return uniform_dist([BEATING_PLAYS[x] for x in modes(opponent([(b, a) for (a, b) in history]))])
    return beater




# This strategy models entry 31025, Byron's CompressorV2
def entry31025(history):
    matchHistory = [opponent_play for opponent_play, my_play in history]
    prediction = uniform_dist("RPS")
    index = 0
    longestMatch = 0
    limit = 50
    while index < len(matchHistory)-1:
        index2 = index
        index3 = len(matchHistory)-1
        length = 0
        while index2 >= 0:
            if matchHistory[index2] != matchHistory[index3]:
                break
            index2 -= 1
            index3 -= 1
            length += 1
            if length > limit:
                break
        if length > longestMatch:
            longestMatch = length
            prediction = singleton_dist(matchHistory[index+1])
        if length > limit:
            break
        index += 1
    return map_dist(prediction, lambda x: {'R':'P', 'P':'S', 'S':'R'}[x])


STRATEGY_TO_PLAY = make_beater(entry31025)



class Player:
    def __init__(self, strategy):
        self.strategy = strategy
        self.history = []

    def play(self):
        self.my_last_play = sample((self.strategy)(self.history))
        return self.my_last_play

    def record_last_opponent_play(self, x):
        self.history.append((x, self.my_last_play))

input = ""
if input == "":
    me = Player(STRATEGY_TO_PLAY)
else:
    me.record_last_opponent_play(input)
output = me.play()