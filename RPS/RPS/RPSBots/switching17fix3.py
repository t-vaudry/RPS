# See http://overview.cc/RockPaperScissors for more information about rock, paper, scissors
# Switching with three different switching strategies

import random

if input == "":
  hist = ""
  opp_played = []
  beat = {'P': 'S', 'S': 'R', 'R': 'P'}
  
  score = {'RR': 0, 'PP': 0, 'SS': 0, 'PR': 1, 'RS': 1, 'SP': 1,'RP': -1, 'SR': -1, 'PS': -1,}
  output = random.choice(["R", "P", "S"])

  candidates = [output] * 6
  # 1. Switch when lose or draw
  # 2. switch when lose
  # 3. Use best overall strategy
  performance = [[(2,0)]*6, [(2,0)]*6, [0]*6]
  main_performance = [0, 0, 0]
  main_candidates = [output] * 3
  indices = [0, 0, 0]
  main_index = 0
else:
  hist += output.lower()+input
  opp_played.append(input)
 
  for i, c in enumerate(candidates):
    performance[0][i] = ({1:performance[0][i][0]+1, 0: 2, -1: 2}[score[c+input]],  
                   performance[0][i][1]+score[c+input])
    performance[1][i] = ({1:performance[1][i][0]+1, 0: performance[1][i][0], -1: 2}[score[c+input]],  
                   performance[1][i][1]+score[c+input])
    performance[2][i] += score[c+input] 

  indices[0] = performance[0].index(max(performance[0], key=lambda x: x[0]**3+x[1]))
  indices[1] = performance[1].index(max(performance[1], key=lambda x: x[0]**3+x[1]))
  indices[2] = performance[2].index(max(performance[2]))

  for i, c in enumerate(main_candidates):
    main_performance[i] += score[c+input]

  main_index = indices[main_performance.index(max(main_performance))]

  for length in range(min(14, len(hist)-2), 0, -2):
    search = hist[-length:]
    idx = hist.rfind(search, 0, -2)
    if idx != -1:
      my = hist[idx+length].upper()
      opp = hist[idx+length+1]
      candidates[0] = beat[opp]
      candidates[1] = beat[beat[my]]
      candidates[2] = opp
      candidates[3] = my
      candidates[4] = beat[beat[opp]]
      candidates[5] = beat[my]
      break
  else:
      output = random.choice(['R', 'P', 'S'])
      candidates = [output] * 6

  for i in range(3):
    main_candidates[i] = candidates[indices[i]]

  output = candidates[main_index]