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
  pokerstats = collections.defaultdict(lambda: 0)

  hist5 = collections.deque()
  stats5 = collections.defaultdict(lambda: collections.defaultdict(lambda: 1))
  poker5 = {'R': 0, 'P': 0, 'S':0}

  hist4 = collections.deque()
  stats4 = collections.defaultdict(lambda: collections.defaultdict(lambda: 1))
  poker4 = {'R': 0, 'P': 0, 'S':0}

  hist3 = collections.deque()
  stats3 = collections.defaultdict(lambda: collections.defaultdict(lambda: 1))
  poker3 = {'R': 0, 'P': 0, 'S':0}

  hist2 = collections.deque()
  stats2 = collections.defaultdict(lambda: collections.defaultdict(lambda: 1))
  poker2 = {'R': 0, 'P': 0, 'S':0}

  hist1 = collections.deque()
  stats1 = collections.defaultdict(lambda: collections.defaultdict(lambda: 1))
  poker1 = {'R': 0, 'P': 0, 'S':0}

  played_probs = {'R': 1, 'P': 1, 'S':1}
  output = random.choice(rps)
  probs = {}
  nothrows = 0
  key = ""
else:
  nothrows += 1
  played_probs[input] += 1
  hist5.append(input)
  hist4.append(input)
  hist3.append(input)
  hist2.append(input)
  hist1.append(input)

  key = tuple(sorted(poker5.values(), reverse=True))
  mmm = "".join([e[0] for e in sorted(poker5.items(), key=operator.itemgetter(1), reverse=True)])
  stats5[key][encode[mmm+input]] += 1
  poker5[input] += 1
  pokerstats[key] += 1

  key = tuple(sorted(poker4.values(), reverse=True))
  mmm = "".join([e[0] for e in sorted(poker4.items(), key=operator.itemgetter(1), reverse=True)])
  stats4[key][encode[mmm+input]] += 1
  poker4[input] += 1

  key = tuple(sorted(poker3.values(), reverse=True))
  mmm = "".join([e[0] for e in sorted(poker3.items(), key=operator.itemgetter(1), reverse=True)])
  stats3[key][encode[mmm+input]] += 1
  poker3[input] += 1

  key = tuple(sorted(poker2.values(), reverse=True))
  mmm = "".join([e[0] for e in sorted(poker2.items(), key=operator.itemgetter(1), reverse=True)])
  stats2[key][encode[mmm+input]] += 1
  poker2[input] += 1

  key = tuple(sorted(poker1.values(), reverse=True))
  mmm = "".join([e[0] for e in sorted(poker1.items(), key=operator.itemgetter(1), reverse=True)])
  stats1[key][encode[mmm+input]] += 1
  poker1[input] += 1

  #probs = played_probs.copy()
  probs = {'R': 1, 'P':1, 'S': 1}
  if len(hist5) > 5:
    rem = hist5.popleft()
    poker5[rem] -= 1
    key = tuple(sorted(poker5.values(), reverse=True))
    mmm = "".join([e[0] for e in sorted(poker5.items(), key=operator.itemgetter(1), reverse=True)])
   
    for t in rps:
      probs[t] *= stats5[key][encode[mmm+t]]

    output = counter_prob(probs)

  if len(hist4) > 4:
    rem = hist4.popleft()
    poker4[rem] -= 1
    key = tuple(sorted(poker4.values(), reverse=True))
    mmm = "".join([e[0] for e in sorted(poker4.items(), key=operator.itemgetter(1), reverse=True)])
   
    for t in rps:
      probs[t] *= stats4[key][encode[mmm+t]]

  if len(hist3) > 3:
    rem = hist3.popleft()
    poker3[rem] -= 1
    key = tuple(sorted(poker3.values(), reverse=True))
    mmm = "".join([e[0] for e in sorted(poker3.items(), key=operator.itemgetter(1), reverse=True)])
   
    for t in rps:
      probs[t] *= stats3[key][encode[mmm+t]]

  if len(hist2) > 2:
    rem = hist2.popleft()
    poker2[rem] -= 1
    key = tuple(sorted(poker2.values(), reverse=True))
    mmm = "".join([e[0] for e in sorted(poker2.items(), key=operator.itemgetter(1), reverse=True)])
   
    for t in rps:
      probs[t] *= stats2[key][encode[mmm+t]]

  if len(hist1) > 1:
    rem = hist1.popleft()
    poker1[rem] -= 1
    key = tuple(sorted(poker1.values(), reverse=True))
    mmm = "".join([e[0] for e in sorted(poker1.items(), key=operator.itemgetter(1), reverse=True)])
   
    for t in rps:
      probs[t] *= stats1[key][encode[mmm+t]]

  output = counter_prob(probs)
  if nothrows == 999:
    for e in pokerstats:
      print e, pokerstats[e]
  else:
    output = random.choice(rps)