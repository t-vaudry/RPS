# See http://overview.cc/RockPaperScissors for more information about rock, paper, scissors
# Similar to switching4 without rndbeat. This should reveal weaknesses of the bot.
# It has some additional strategies, which are combinations of old ones.
# The strategy selection is changed to those of the newer switching bots.

import random

if input == "":
  # combinations not in Python 2.5, so I have to define it myself
  def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
      return
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
      for i in reversed(range(r)):
        if indices[i] != i + n - r:
          break
      else:
        return
      indices[i] += 1
      for j in range(i+1, r):
        indices[j] = indices[j-1] + 1
      yield tuple(pool[i] for i in indices)

  hist = ""
  opp_played = []
  beat = {'P': 'S', 'S': 'R', 'R': 'P'}
  beat2 = {'PP': 'S', 'SS': 'R', 'RR':'P', 'PS': 'S', 'PR': 'P', 'RS': 'R', 'RP': 'P', 'SP': 'S', 'SR': 'R'}
  
  score = {'RR': 0, 'PP': 0, 'SS': 0, 'PR': 1, 'RS': 1, 'SP': 1,'RP': -1, 'SR': -1, 'PS': -1,}
  output = random.choice(["R", "P", "S"])

  candidates = [output] * 21
  performance = [(0,0)] * 21
else:
  hist += output.lower()+input
  opp_played.append(input)
 
  for i, c in enumerate(candidates):
    performance[i] = ({1:performance[i][0]+1, 0: performance[i][0], -1: 0}[score[c+input]],  
                   performance[i][1]+score[c+input])

  index = performance.index(max(performance, key=lambda x: x[0]**3+x[1]))

  for length in range(min(10, len(hist)-2), 0, -2):
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
      for i, (a,b) in enumerate(combinations(candidates[:6],2)):
        candidates[6+i] = beat2[a+b]
      break
  else:
      candidates = [random.choice(['R', 'P', 'S'])] * 21
 
  output = candidates[index]