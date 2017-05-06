# credit to pyfex
#I only changed a little bit from what pyfex did to see if it might work differently
# For example, I changed how the random call up works.
from random import choice
if input == "":
  hist = ""
  opp_played = []
  beat = {'P': 'S', 'S': 'R', 'R': 'P'}
  beat2 = {'PP': 'S', 'SS': 'R', 'RR':'P', 'PS': 'S', 'PR': 'P', 'RS': 'R', 'RP': 'P', 'SP': 'S', 'SR': 'R'}
  complement = {'PS': 'R', 'PR': 'S', 'RS': 'P', 'RP': 'S', 'SP': 'R', 'SR': 'P'}
  
  score = {'RR': 0, 'PP': 0, 'SS': 0, 'PR': 1, 'RS': 1, 'SP': 1,'RP': -1, 'SR': -1, 'PS': -1,}
  
  output = choice(["R", "P", "S"])

  candidate1 = [output, output]
  candidate2 = [output] * 5
  performance1 = [0, 0]
  performance2 = [(0,0)] * 5
else:
  hist += output.lower()+input
  opp_played.append(input)
  performance1[0] += score[candidate1[0]+input]
  performance1[1] += score[candidate1[1]+input]
  
  for i, p in enumerate(candidate2):
    performance2[i] = ({1:performance2[i][0]+1, 0: performance2[i][0], -1: 0}[score[p+input]],  
                   performance2[i][1]+score[p+input])

  index1 = performance1.index(max(performance1))
  index2 = performance2.index(max(performance2, key=lambda x: x[0]**3+x[1]))
  candidate1[1] = beat[choice(opp_played)]
  
  for length in range(min(10, len(hist)-2), 0, -2):
    search = hist[-length:]
    idx = hist.rfind(search, 0, -2)
    if idx != -1:
      my = hist[idx+length].upper()
      opp = hist[idx+length+1]
      candidate2[0] = beat[opp]
      candidate2[1] = beat[beat[my]]
      candidate2[2] = beat2[beat[my] + beat[beat[opp]]]
      candidate2[3] = beat2[beat[opp] + beat[beat[my]]]
      candidate2[4] = complement[''.join(sorted(set(candidate2[0] + candidate2[1] + candidate2[3])))]
      break
  else:
      candidate = [choice(['R', 'P', 'S'])] * 5
 
  candidate1[0] = candidate2[index2]
  
  output = candidate1[index1]