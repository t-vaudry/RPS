import random

if input == "":
  counter = {'P': 'S', 'R': 'P', 'S':'R'}
  score = {'RR': 0, 'PP': 0, 'SS': 0, 'PR': 1, 'RS': 1, 'SP': 1,'RP': -1, 'SR': -1, 'PS': -1,}
  opp_played = []
  me_played = []
  output = random.choice(['R', 'P', 'S'])
  candidates = [output, output]
  performance = [0, 0]
else:
  opp_played.append(input)
  me_played.append(input)

  performance[0] += score[candidates[0]+output]
  performance[1] += score[candidates[1]+output]

  idx = performance.index(max(performance))

  candidates[0] = counter[random.choice(opp_played)]
  candidates[1] = counter[counter[random.choice(me_played)]]

  output = candidates[idx]