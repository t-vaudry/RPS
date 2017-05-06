from collections import defaultdict
import random
from pprint import pprint

def beat(move):
    if move == 'R':
        return 'P'
    elif move == 'S':
        return 'R'
    elif move == 'P':
        return 'S'
    
def random_move():
    return random.choice(['R', 'P', 'S'])

class PredictN:
    lookback = 1
    history = ""
    frequency = {}
    
    def __init__(self, lookback = 1):
        self.lookback = lookback
        
    def __str__(self):
        return "Predict{0}".format(self.lookback)
    
    def add_history(self, move):
        self.history += move
        
        if len(self.history) > self.lookback:
            key = self.history[(self.lookback + 1) * -1:-1]
            if key not in self.frequency:
                self.frequency[key] = defaultdict(int)
            
            self.frequency[key][move] += 1
    
    def predict(self):
        if self.lookback == 0:
            return (random_move(), 0.5)
        
        key = self.history[(self.lookback) * -1:]
        if key not in self.frequency:
            return (random_move(), 0.5)
        else:
            distribution = self.frequency[key]
            all_sum = sum(distribution.values())
            max_count = max(distribution.values())
            max_key = list(filter(lambda k: distribution[k] == max_count, distribution.keys()))[0]
            
            return (max_key, max_count / all_sum)
                    
    def print_frequency(self):
        pprint(self.frequency)
 
if input == "":
    predictors = [PredictN(0), PredictN(1), PredictN(2), PredictN(3), PredictN(4), PredictN(5), PredictN(6)]
    tallies = {}
    for p in predictors:
        tallies[p] = 0
    last_predictor = None
    predictions = []
    output = random_move()
else:
    for p in predictors:
        p.add_history(input)
      
    if len(predictions) > 0:
        for k in range(len(predictions)):
            if predictions[k] == input:
                tallies[predictors[k]] += 1
            
    predictions = [p.predict()[0] for p in predictors]
    max_tally = max(tallies.values())
    predictor_with_max_tally = list(filter(lambda k: tallies[k] == max_tally, tallies.keys()))[0]
    output = beat(predictions[predictors.index(predictor_with_max_tally)])