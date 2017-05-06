if input == "":
  import random
  from collections import defaultdict
  
  beat = {'P': 'S', 'R': 'P', 'S':'R'}
  rps = ['R', 'P', 'S']
  hist = ""
  opp_hist = []
  patterns = defaultdict(list)  
  output = random.choice(rps)

else:
  opp_hist.append(input)
  for length in range(2, min(12, len(hist)), 2):
    patterns[hist[-length:]].append(output + input)
  hist += output + input

  for length in range(min(10, len(hist)), 0, -2):
    p = patterns[hist[-length:]]
    if len(p) >= 2:
      output = beat[random.choice(p)[1]]
      break
  else:
    output = random.choice(opp_hist)