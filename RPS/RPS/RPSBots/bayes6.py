# See http://overview.cc/RockPaperScissors for more information about rock, paper, scissors

from collections import defaultdict
import operator
import random

if input == "":
  score = {'RR': 0, 'PP': 0, 'SS': 0, 'PR': 1, 'RS': 1, 'SP': 1,'RP': -1, 'SR': -1, 'PS': -1,}
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

  played_probs = defaultdict(lambda: 1)
  opp_probs = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 1)))
  my_probs = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 1)))
  both_probs = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 1)))

  patterndict = defaultdict(str)

  output = random.choice(["R", "P", "S"])
  hist = ""
  answers = []
else:

  for length in range(min(16, len(hist)), 0, -2):
    pattern = patterndict[hist[-length:]]
    patterndict[hist[-length:]] += output + input

  played_probs[input] += 1

  for i, answer in enumerate(answers):
    my = answer[0]
    opp = answer[1]

    opp_probs[i][opp][input] += 1
    my_probs[i][my][input] += 1
    both_probs[i][my+opp][input] += 1

  hist += output + input

  answers = []

  for length in range(2, 16, 2):
    pattern = patterndict[hist[-length:]]
    if pattern != "":
      answers.append(pattern[-2:])
      break

  probs = {}
  for hand in rps:
    probs[hand] = played_probs[hand]
        
  for i,answer in enumerate(answers):
    my = answer[0]
    opp = answer[1]
    for hand in rps:
      probs[hand] *= opp_probs[i][opp][hand] * my_probs[i][my][hand] * both_probs[i][my+opp][hand]
                
  output = counter_prob(probs)