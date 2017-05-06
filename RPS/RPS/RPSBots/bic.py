import random
from collections import defaultdict

class TieredMarkov:
  def __init__(self, order, dampen):
    self.order = order
    self.dampen = dampen
    self.chains = [NMarkov(i+1) for i in range(0,order)]

  def dump_data(self):
    return [chain.dump_data() for chain in self.chains]
  
  def get_counts(self, state):
    counts = [self.chains[i].get_counts(state) for i in range(0,self.order)]
    keys = set(key for d in counts for key in d.keys())
    merged = dict((key, sum(counts[i].get(key,0) * self.dampen ** i for i in range(len(counts)))) for key in keys)
    return merged
  
  def add_point(self, state, next):
    [chain.add_point(state, next) for chain in self.chains]

class NMarkov:
  def __init__(self, order):
    self.order = order
    self.state_counts_map = {}

  def dump_data(self):
    return self.state_counts_map

  def get_key(self, state):
    return str(state[-self.order:])

  def get_counts(self, state):
    key = self.get_key(state)
    if key not in self.state_counts_map:
      return {}
    return self.state_counts_map[key]

  def add_point(self, state, next):
    state = state[-self.order:]
    if len(state) == self.order:

      key = self.get_key(state)
      if key not in self.state_counts_map:
        self.state_counts_map[key] = {}

      counts = self.state_counts_map[key]
      if next not in counts:
        counts[next] = 0
      counts[next] += 1

class MarkovFeeder:
  def __init__(self, markov):
    self.markov = markov
    self.history = []

  def dump_data(self):
    return self.markov.dump_data()

  def add_point(self, input, output):
    self.history.append(input)
    self.markov.add_point(self.history, output)

  def get_counts(self, state):
    return self.markov.get_counts(state)


class RPSPatternMatcher:
  def __init__(self, order):
    self.order = order
    self.combined_response = MarkovFeeder(TieredMarkov(order, 9))
    self.victory_response = MarkovFeeder(TieredMarkov(order, 27))
    self.opponent_response = MarkovFeeder(TieredMarkov(order, 27))
    self.history = []

  def dump_data(self):
    return [ self.combined_response.dump_data()
           , self.victory_response.dump_data()
           , self.opponent_response.dump_data()]

  def register_throw(self,our_throw, opponent_throw):
    if self.history:
      our_last, opponent_last = self.history[-1]
      self.combined_response.add_point(our_last * 3 + opponent_last, opponent_throw)
      self.victory_response.add_point((opponent_last - our_last + 3) % 3, (opponent_throw - opponent_last + 3) % 3)
      self.opponent_response.add_point(opponent_last, opponent_throw)

    self.history.append((our_throw, opponent_throw))

  def next_throw(self):
    our_last, opponent_last = self.history[-1]
    victory_offset_counts = self.victory_response.get_counts([(b - a + 3) % 3 for a,b in self.history[-self.order:]])
    victory_counts = dict(((opponent_last + key + 3) % 3, val) for key, val in victory_offset_counts.items())
    combined_counts = dict((key, val*3) for key, val in 
      self.combined_response.get_counts([a*3 + b for a,b in self.history[-self.order:]]).items())
    opponent_counts = self.opponent_response.get_counts([b for a,b in self.history[-self.order:]])
    d_list = [ victory_counts
             , combined_counts
             , opponent_counts
             ]
    total_counts = [sum(d.get(i,0) for d in d_list) for i in range(3)]

    if sum(total_counts) == 0:
      return random.choice(range(3))

    total_scores = [max([total_counts[(i+2)%3] - total_counts[(i+1)%3],0]) for i in range(3)]
    rand = random.random() * sum(total_scores)
    for i, weight in enumerate(total_scores):
      rand -= weight
      if rand <= 0:
        return i

if input == "":
  types = ["R", "P", "S"]
  matcher = RPSPatternMatcher(4)
  last_throw = 0

if input in types:
  matcher.register_throw(last_throw, types.index(input))
  last_throw = matcher.next_throw()
else:
  last_throw = random.choice(range(3))
output = types[last_throw]