# See http://overview.cc/RockPaperScissors for more information about rock, paper, scissors

if input == "":
  import random
  score = {'RR': 0, 'PP': 0, 'SS': 0, 'PR': 1, 'RS': 1, 'SP': 1,'RP': -1, 'SR': -1, 'PS': -1,}
  beat = {'P': 'S', 'R': 'P', 'S':'R'}
  rps = ['R', 'P', 'S']
  hist = {0: [], -1: [], 1:[]}  
  output = random.choice(rps)

else:
  sc = score[output+input]
  hist[sc].append(input)
  output = random.choice(hist[sc])