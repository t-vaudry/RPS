# See http://overview.cc/RockPaperScissors for more information about rock, paper, scissors
# Switching with patterns of patterns. I have already used this is in the bayes bots. Now I will
# try it in a switching bots too

import random
import operator
from collections import defaultdict

if input == "":
  both_hist = ""
  my_hist = ""
  opp_hist = ""
  beat = {'P': 'S', 'S': 'R', 'R': 'P'}
  cede = {'P': 'R', 'S': 'P', 'R': 'S'}

  both_patterns = defaultdict(str)
  opp_patterns = defaultdict(str)
  my_patterns = defaultdict(str)

  both2_patterns = defaultdict(str)
  opp2_patterns = defaultdict(str)
  my2_patterns = defaultdict(str)

  score = {'RR': 0, 'PP': 0, 'SS': 0, 'PR': 1, 'RS': 1, 'SP': 1,'RP': -1, 'SR': -1, 'PS': -1,}
  output = random.choice(["R", "P", "S"])

  candidates = [output] * 36

  performance = [(2,0)] * 36

else:

  both_hist += output+input
  my_hist += output
  opp_hist += input

  for length in range(min(5, len(my_hist)), 0, -1):
    p = opp_patterns[opp_hist[-length:]]
    if p != "":
      for length2 in range(min(5, len(p)), 0, -1):
        opp2_patterns[p[-2*length2:]] += output + input
    opp_patterns[opp_hist[-length:]] += output + input

    p = my_patterns[my_hist[-length:]]
    if p != "":
      for length2 in range(min(5, len(p)), 0, -1):
        my2_patterns[p[-2*length2:]] += output + input
    my_patterns[my_hist[-length:]] += output + input

    p = both_patterns[both_hist[-2*length:]]
    if p != "":
      for length2 in range(min(5, len(p)), 0, -1):
        both2_patterns[p[-2*length2:]] += output + input
    both_patterns[both_hist[-2*length:]] += output + input

  for i, c in enumerate(candidates):
    performance[i] = ({1:performance[i][0]+1, 0: 2, -1: 2}[score[c+input]],  
                      performance[i][1]+score[c+input])

  output = random.choice(['R', 'P', 'S'])
  candidates = [output] * 36

  index = performance.index(max(performance, key=lambda x: x[0]**3+x[1]))

  for length in range(min(5, len(my_hist)), 0, -1):
    pattern = both_patterns[both_hist[-2*length:]]
    if pattern != "":
      opp = pattern[-1]
      my = pattern[-2]
      candidates[0] = beat[opp]
      candidates[1] = cede[my]
      candidates[2] = opp
      candidates[3] = my
      candidates[4] = cede[opp]
      candidates[5] = beat[my]
      for length2 in range(min(5, len(pattern)), 0, -1):
        pattern2 = both2_patterns[pattern[-2*length2:]]
        if pattern2 != "":
          my2 = pattern2[-2]
          opp2 = pattern2[-1]
          candidates[6] = beat[opp2]
          candidates[7] = cede[my2]
          candidates[8] = opp2
          candidates[9] = my2
          candidates[10] = cede[opp2]
          candidates[11] = beat[my2]
          break
      break

  for length in range(min(5, len(my_hist)), 0, -1):
    pattern = my_patterns[my_hist[-length:]]
    if pattern != "":
      opp = pattern[-1]
      my = pattern[-2]
      candidates[12] = beat[opp]
      candidates[13] = cede[my]
      candidates[14] = opp
      candidates[15] = my
      candidates[16] = cede[opp]
      candidates[17] = beat[my]
      for length2 in range(min(5, len(pattern)), 0, -1):
        pattern2 = my2_patterns[pattern[-2*length2:]]
        if pattern2 != "":
          my2 = pattern2[-2]
          opp2 = pattern2[-1]
          candidates[18] = beat[opp2]
          candidates[19] = cede[my2]
          candidates[20] = opp2
          candidates[21] = my2
          candidates[22] = cede[opp2]
          candidates[23] = beat[my2]
          break
      break

  for length in range(min(5, len(opp_hist)), 0, -1):
    p = opp_patterns[opp_hist[-length:]]
    if pattern != "":
      opp = pattern[-1]
      my = pattern[-2]
      candidates[24] = beat[opp]
      candidates[25] = cede[my]
      candidates[26] = opp
      candidates[27] = my
      candidates[28] = cede[opp]
      candidates[29] = beat[my]
      for length2 in range(min(5, len(pattern)), 0, -1):
        pattern2 = my2_patterns[pattern[-2*length2:]]
        if pattern2 != "":
          my2 = pattern2[-2]
          opp2 = pattern2[-1]
          candidates[30] = beat[opp2]
          candidates[31] = cede[my2]
          candidates[32] = opp2
          candidates[33] = my2
          candidates[34] = cede[opp2]
          candidates[35] = beat[my2]
          break
      break

  output = candidates[index]