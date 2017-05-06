from collections import defaultdict
import operator
import random

if input == "":
  score = {'RR': 0, 'PP': 0, 'SS': 0, 'PR': 1, 'RS': 1, 'SP': 1,'RP': -1, 'SR': -1, 'PS': -1,}
  rps = ['R', 'P', 'S']  
  def counter_prob(probs):
    weighted_list = []
    for h in rps:
      weighted = 0
      for p in probs.keys():
        points = score[h+p]
        prob = probs[p]
        weighted += points * prob
        weighted_list.append((h, weighted))

    return max(weighted_list, key=operator.itemgetter(1))[0]

  played_probs = defaultdict(lambda: 1)
  opp_probs = defaultdict(lambda: defaultdict(lambda: 1))
  my_probs = defaultdict(lambda: defaultdict(lambda: 1))
  both_probs = defaultdict(lambda: defaultdict(lambda: 1))

  myhist_opp_probs = defaultdict(lambda: defaultdict(lambda: 1))
  myhist_my_probs = defaultdict(lambda: defaultdict(lambda: 1))
  myhist_both_probs = defaultdict(lambda: defaultdict(lambda: 1))

  opphist_opp_probs = defaultdict(lambda: defaultdict(lambda: 1))
  opphist_my_probs = defaultdict(lambda: defaultdict(lambda: 1))
  opphist_both_probs = defaultdict(lambda: defaultdict(lambda: 1))

  output = random.choice(rps)
  hist = "" 
  my_hist = ""
  opp_hist = ""
  my = opp = myhist_my = myhist_opp = opphist_my = opphist_opp = ""
else:
  played_probs[input] += 1

  opp_probs[opp][input] += 1
  my_probs[my][input] += 1
  both_probs[my+opp][input] += 1

  myhist_opp_probs[myhist_opp][input] += 1
  myhist_my_probs[myhist_my][input] += 1
  myhist_both_probs[myhist_my+myhist_opp][input] += 1

  opphist_opp_probs[opphist_opp][input] += 1
  opphist_my_probs[opphist_my][input] += 1
  opphist_both_probs[opphist_my+opphist_opp][input] += 1

  hist += output.lower() + input
  my_hist += output
  opp_hist += input

  my = opp = myhist_my = myhist_opp = opphist_my = opphist_opp = ""
  probs = {}
  for hand in rps:
    probs[hand] = played_probs[hand]

  for length in range(min(10, len(hist)-2), 0, -2):
    search = hist[-length:]
    idx = hist.rfind(search, 0, -2)
    if idx != -1:
      my = hist[idx+length].upper()
      opp = hist[idx+length+1]
      for hand in rps:
        probs[hand] *= opp_probs[opp][hand] * my_probs[my][hand] * both_probs[my+opp][hand] 
      break

  for length in range(min(5, len(my_hist)-1), -1):
    my_search = my_hist[-length:]
    idx = my_hist.rfind(my_search, 0, -1)
    if idx != -1:
      myhist_my = my_hist[idx+length]
      myhist_opp = opp_hist[idx+length]
      for hand in rps:
        probs[hand] *= myhist_probs[myhist_opp][hand] * myhist_probs[myhist_my][hand] * myhist_probs[myhist_my+myhist_opp][hand]
      break

  for length in range(min(5, len(opp_hist)-1), -1):
    opp_search = opp_hist[-length:]
    idx = opp_hist.rfind(opp_search, 0, -1)
    if idx != -1:
      opphist_my = my_hist[idx+length]
      opphist_opp = opp_hist[idx+length]
      for hand in rps:
        probs[hand] *= opphist_probs[opphist_opp][hand] * opphist_probs[opphist_my][hand] * opphist_probs[opphist_my+opphist_opp][hand]
      break

  output = counter_prob(probs)