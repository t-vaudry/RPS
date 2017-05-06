# See http://overview.cc/RockPaperScissors for more information about rock, paper, scissors
# Bayes/Switching Hybrid. Use bayes statistic to choose the strategy.

from collections import defaultdict
import operator
import random

if input == "":
  score = {'RR': 0, 'PP': 0, 'SS': 0, 'PR': 1, 'RS': 1, 'SP': 1,'RP': -1, 'SR': -1, 'PS': -1,}
  p_add = {'RR': 1, 'PP': 1, 'SS': 1, 'PR': 0, 'RS': 0, 'SP': 0,'RP': 0, 'SR': 0, 'PS': 0,}
  beat = {'P': 'S', 'S': 'R', 'R': 'P'}
  cede = {'P': 'R', 'S': 'P', 'R': 'S'}
  rps = ['R', 'P', 'S']
  
  def counter_prob(probs):
    weighted_list = []
    for h in ['R', 'P', 'S']:
      weighted = 0
      for p in probs.keys():
        points = score[h+p]
        prob = probs[p]
        weighted += points * prob
        weighted_list.append((h, weighted))

    return max(weighted_list, key=operator.itemgetter(1))[0]

  patterndict = defaultdict(str)
  played_probs = defaultdict(lambda: 1)

  prediction = []
  performance = [1] * 6

  hist = "" 
  my = opp = ""

  output = random.choice(["R", "P", "S"])

else:
  played_probs[input] += 1
  for i, p in enumerate(prediction):
    performance[i] += p_add[p+input]

  for length in range(min(14, len(hist)), 0, -2):
    pattern = patterndict[hist[-length:]]
    patterndict[hist[-length:]] += output + input

  hist += output + input
  my = opp = ""

  for length in range(min(14, len(hist)), 0, -2):
    pattern = patterndict[hist[-length:]]
    if pattern != "":
      my = pattern[-2]
      opp = pattern[-1]
      break

  probs = {}
  for hand in rps:
    probs[hand] = played_probs[hand]
        
  if my and opp:
    prediction = [opp, beat[opp], cede[opp], my, cede[my], beat[my]] 
    for hand in rps:
      probs[hand] *= reduce(operator.mul, [performance[i] for i, p in enumerate(prediction) if p == hand])
  else:
    prediction = []
                
  output = counter_prob(probs)