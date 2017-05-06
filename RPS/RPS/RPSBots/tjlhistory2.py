from __future__ import division
import random
import itertools


OPTIONS = ["R", "P", "S"]
BEAT = {
  "R": "P",
  "P": "S",
  "S": "R",
}

ALPHA = (1/3) + 0.02

def product(*args, **kwds):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = map(tuple, args) * kwds.get('repeat', 1)
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)


class MarkovPredictor:
   '''
   Using the markov assumption with k=length, count n-sequences.
   Allow requests for predictions of the most likely next state
   '''
   
   def __init__(self, options, length):
      self.options = options
      self.length = length
      self.history = []
      self.counts = {}
      self.total = 0

      # LaPlace Smooth
      all_seqs = product(options, repeat=length)
      for ngram in all_seqs:
         self.counts[ngram] = 1
         self.total += 1
       

   def observe(self, item):
      self.history.append(item)
      if len(self.history) > self.length:
         self.history.pop(0)

      if len(self.history) == self.length:
         ngram = tuple(self.history)
         if ngram in self.counts:
            self.counts[ngram] +=  1
            self.total += 1
         else:
            print "%s not in %s" % (str(ngram), str(self.counts))

   def predict(self):
    
      if len(self.history) < self.length:
         return None, 0
       
      counts = {}
      total = 0
      for option in self.options:
         ngram = tuple(self.history[-1 * (self.length - 1):]) + (option,)
         counts[option] = self.counts[ngram]
         total += counts[option]

      best_option = None
      best_chance = 0
      for option in self.options:
         chance = counts[option] / total
         if chance > best_chance:
            best_chance = chance
            best_option = option

      return best_option, best_chance


def get_best_choice(predictors):

    best_choice = None
    best_chance = 0

    choices = [p.predict() for p in predictors]

    for choice, chance in choices:
       if chance > best_chance:
          best_chance = chance
          best_choice = choice

    return best_choice, best_chance

# Base strategy: make a random move
output = random.choice(OPTIONS)


if input == '':
    # Hypothesis: people think about 6 moves back when playing
    predictors = [MarkovPredictor(OPTIONS, length) for length in range(2,6)]
    
    # Hypothesis: need to avoid my own predictable moves
    my_predictors = [MarkovPredictor(OPTIONS, length) for length in range(2,6)]

else:
    for p in predictors:
       p.observe(input)

    their_choice, their_chance = get_best_choice(predictors)
    my_choice, my_chance = get_best_choice(my_predictors)
   
    # Beat predictable moves 
    if their_chance - ALPHA > 0:
        output = BEAT[their_choice]

    # But it's more important to be unpredictable yourself
    if my_chance - ALPHA > 0:
        output = BEAT[BEAT[my_choice]]

for p in my_predictors:
  p.observe(output)