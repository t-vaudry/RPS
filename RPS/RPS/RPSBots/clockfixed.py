import random

if input == "":
  counter = {'P': 'S', 'S': 'R', 'R': 'P'}
  clock = {'P': 'R', 'R': 'S', 'S': 'P'}
  output =  random.choice(["R", "P", "S"])
  last_score = 0
  last_opp = random.choice(["R", "P", "S"])
  last_me = random.choice(["R", "P", "S"])
  score = {'RR': 0, 'PP': 0, 'SS': 0, 'PR': 1, 'RS': 1, 'SP': 1,'RP': -1, 'SR': -1, 'PS': -1,}
  tie_candidates = ['P', 'P', 'P', 'P', 'P', 'P']
  tie_performance = [0, 0, 0, 0, 0, 0]
  win_candidates = ['P', 'P', 'P', 'P', 'P', 'P']
  win_performance = [0, 0, 0, 0, 0, 0]
  lose_candidates = ['P', 'P', 'P', 'P', 'P', 'P']
  lose_performance = [0, 0, 0, 0, 0, 0]
else:
  #update performance of last move
  last_sc = score[last_me+last_opp]
  if last_sc == 0:
    for i, c in enumerate(tie_candidates):
      s = score[c+output]
      if s == 1:
        tie_performance[i] += 1
      elif s == -1:
        tie_performance[i] = 0
  elif last_sc == 1:
    for i, c in enumerate(win_candidates):
      s = score[c+output]
      if s == 1:
        win_performance[i] += 1
      elif s == -1:
        win_performance[i] = 0
  elif last_sc == -1:
    for i, c in enumerate(lose_candidates):
      s = score[c+output]
      if s == 1:
        lose_performance[i] += 1
      elif s == -1:
        lose_performance[i] = 0

  # update candidates and choose index with best performance
  sc = score[output+input]
  if sc == 0:
    tie_candidates[0] = input
    tie_candidates[1] = counter[input]
    tie_candidates[2] = clock[input]
    tie_candidates[3] = input
    tie_candidates[4] = counter[output]
    tie_candidates[5] = clock[output]
    m = max(tie_performance)
    idx = tie_performance.index(m)
    output = tie_candidates[idx]
  elif sc == 1:
    win_candidates[0] = input
    win_candidates[1] = counter[input]
    win_candidates[2] = clock[input]
    win_candidates[3] = input
    win_candidates[4] = counter[output]
    win_candidates[5] = clock[output]
    m = max(win_performance)
    idx = win_performance.index(m)
    output = win_candidates[idx]
  elif sc == -1:
    lose_candidates[0] = input
    lose_candidates[1] = counter[input]
    lose_candidates[2] = clock[input]
    lose_candidates[3] = input
    lose_candidates[4] = counter[output]
    lose_candidates[5] = clock[output]
    m = max(lose_performance)
    idx = lose_performance.index(m)
    output = lose_candidates[idx]

  last_opp = input
  last_me = output