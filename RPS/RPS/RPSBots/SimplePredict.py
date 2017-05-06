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
    
class PredictN:
    lookback = 1
    history = ""
    frequency = {}
    
    def __init__(self, lookback = 1):
        self.lookback = lookback
        
    def add_history(self, move):
        self.history += move
        
        if len(self.history) > self.lookback:
            key = self.history[(self.lookback + 1) * -1:-1]
            if key not in self.frequency:
                self.frequency[key] = defaultdict(int)
            
            self.frequency[key][move] += 1
    
    def predict(self):
        key = self.history[(self.lookback) * -1:]
        if key not in self.frequency:
            return (random.choice(['R', 'P', 'S']), 0.5)
        else:
            distribution = self.frequency[key]
            all_sum = sum(distribution.values())
            max_count = max(distribution.values())
            max_key = list(filter(lambda k: distribution[k] == max_count, distribution.keys()))[0]
            
            return (max_key, max_count / all_sum)
                    
    def print_frequency(self):
        pprint(self.frequency)
 
try:
    predictors
except NameError:
    predictors = [PredictN(1), PredictN(2), PredictN(3), PredictN(4)]
    
for p in predictors:
    if len(input) > 0:
        p.add_history(input)
    
predictions = [p.predict() for p in predictors]
max_prediction = max(p[1] for p in predictions)
max_move = list(filter(lambda p: p[1] == max_prediction, predictions))[0][0]

if max_prediction < 0.5:
    predicted_move = random.choice(['R', 'P', 'S'])
else:
    predicted_move = beat(max_move)

output = beat(predicted_move)