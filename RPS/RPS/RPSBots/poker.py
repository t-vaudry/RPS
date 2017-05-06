# See http://overview.cc/RockPaperScissors for more information about rock, paper, scissors

import random
import operator
import collections

if input == "":
  rps = ['R', 'P', 'S']
  score = {'RR': 0, 'PP': 0, 'SS': 0, 'PR': 1, 'RS': 1, 'SP': 1,'RP': -1, 'SR': -1, 'PS': -1,}

  def counter_prob(probs):
    weighted_list = []
    for h in rps:
      weighted = 0
      for p in probs.keys():
        points = score[h+p]
        prob = probs[p]
        weighted += points * prob
      weighted_list.append((h, weighted))
    ret = max(weighted_list, key=operator.itemgetter(1))[0]
    return ret

  encode = {
            'RPSR': 0, 'RPSP':1, 'RPSS': 2, 
            'RSPR': 0, 'RSPP':2, 'RSPS': 1,
            'PRSR': 1, 'PRSP':0, 'PRSS': 2, 
            'PSRR': 2, 'PSRP':0, 'PSRS': 1, 
            'SRPR': 1, 'SRPP':2, 'SRPS': 0, 
            'SPRR': 2, 'SPRP':1, 'SPRS': 0, 
           }
  beat = {'R': 'P', 'P':'S', 'S':'R'}
  stats = collections.defaultdict(lambda: collections.defaultdict(lambda: 1))
  pokerstats = collections.defaultdict(lambda: 0)
  hist = collections.deque()
  poker = {'R': 0, 'P': 0, 'S':0}
  output = random.choice(rps)
else:
  hist.append(input)
  key = tuple(sorted(poker.values(), reverse=True))
  mmm = "".join([e[0] for e in sorted(poker.items(), key=operator.itemgetter(1), reverse=True)])
  stats[key][encode[mmm+input]] += 1
  pokerstats[key] += 1
  poker[input] += 1
  if len(hist) > 5:
    rem = hist.popleft()
    poker[rem] -= 1
    key = tuple(sorted(poker.values(), reverse=True))
    mmm = "".join([e[0] for e in sorted(poker.items(), key=operator.itemgetter(1), reverse=True)])
   
    probs = {}
    for t in rps:
      probs[t] = stats[key][encode[mmm+t]]

    output = counter_prob(probs)
  else:
    output = random.choice(rps)