# See http://overview.cc/RockPaperScissors for more information about rock, paper, scissors

import random
import operator
import collections

if input == "":
  rps = ['R', 'P', 'S']
  score = {'RR': 0, 'PP': 0, 'SS': 0, 'PR': 1, 'RS': 1, 'SP': 1,'RP': -1, 'SR': -1, 'PS': -1,}
  encode = { 'RR': 'a', 'PP': 'b', 'SS': 'c', 'PR': 'd', 'RS': 'f', 'SP': 'g','RP': 'h', 'SR': 'i', 'PS': 'j',}

  def counter_prob(probs):
    weighted_list = []
    total = (probs['R'] + probs['S'] + probs['P'] + .0) * 2
    for h in rps:
      weighted = 0
      for p in probs.keys():
        points = score[h+p] + 1
        prob = probs[p]
        weighted += points * prob
      weighted_list.append((h, weighted))
      total += weighted
    best, best_perc = max(weighted_list, key=operator.itemgetter(1))
    best_perc /= total 
    return best, best_perc

  hist = collections.deque()
  poker = collections.defaultdict(lambda: 1)
  output = random.choice(rps)
  probs = {}
  nothrows = 0
  played = 0
  total_score = 0
else:
  total_score += score[output + input]
  nothrows += 1
  for i in range(1, 6):
    pokerkey = "".join(sorted(list(hist)[-i:]))
    poker[pokerkey+input] += 1
  hist.append(encode[output+input])
  if len(hist) > 5:
    hist.popleft()
    probs = {'R': 1, 'P': 1, 'S': 1}
    for i in range(1, 6):
      pokerkey = "".join(sorted(list(hist)[-i:]))
      for t in rps:
        probs[t] *= poker[pokerkey+t] 

    output, percentage = counter_prob(probs)
  else:
    output = random.choice(rps)