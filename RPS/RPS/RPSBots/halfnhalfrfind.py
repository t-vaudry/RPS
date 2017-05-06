from collections import defaultdict
import random

if input == "":
  hist = ""
  rps = ['R', 'P', 'S']
  counter = {'P': 'S', 'S': 'R', 'R': 'P'}
  stats = defaultdict(lambda: 0)
  output = random.choice(rps)
  my = opp = ""
else:
  hist += output.lower()+input
  stats[my+opp+input] += 1
  for length in range(min(10, len(hist)-2), 0, -2):
    search = hist[-length:]
    idx = hist.rfind(search, 0, -2)
    if idx != -1:
      my = hist[idx+length].upper()
      opp = hist[idx+length+1]
      break
  predictions = [stats[my+opp+h] for h in rps]
  prediction = rps[predictions.index(max(predictions))]
  output = counter[prediction]