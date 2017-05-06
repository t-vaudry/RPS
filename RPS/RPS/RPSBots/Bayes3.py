from collections import defaultdict
import operator
import random

if input == "":
  score = {'RR': 0, 'PP': 0, 'SS': 0, 'PR': 1, 'RS': 1, 'SP': 1,'RP': -1, 'SR': -1, 'PS': -1,}
  
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

  played_probs = defaultdict(lambda: 0)
  opp_probs = defaultdict(lambda: defaultdict(lambda: 0))
  my_probs = defaultdict(lambda: defaultdict(lambda: 0))
  both_probs = defaultdict(lambda: defaultdict(lambda: 0))

  output = random.choice(["R", "P", "S"])
  hist = "" 
  my = opp = ""
else:
  played_probs[input] += 1
  opp_probs[opp][input] += 1
  my_probs[my][input] += 1
  both_probs[my+opp][input] += 1
  hist += output.lower() + input
  for length in range(min(8, len(hist)-2), 0, -2):
    search = hist[-length:]
    idx = hist.rfind(search, 0, -2)
    if idx != -1:
      my = hist[idx+length].upper()
      opp = hist[idx+length+1]
      probs = defaultdict(lambda: 0)
      for hand in ["R", "P", "S"]:
        probs[hand] = played_probs[hand] * opp_probs[opp][hand] * my_probs[my][hand] * both_probs[my+opp][input] 
      output = counter_prob(probs)
      break
  else:
    output = random.choice(["R", "P", "S"])