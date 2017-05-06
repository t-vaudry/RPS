# See http://overview.cc/RockPaperScissors for more information about rock, paper, scissors
# Similar to switching7 with another strategy selection and an additional predictor

import random

if input == "":
  hist = ""
  opp_played = []
  counter = {'P': 'S', 'S': 'R', 'R': 'P'}
  score = {'RR': 0, 'PP': 0, 'SS': 0, 'PR': 1, 'RS': 1, 'SP': 1,'RP': -1, 'SR': -1, 'PS': -1,}
  output = random.choice(["R", "P", "S"])

  predict1 = [output, output]
  predict2 = [output] * 7
  correct1 = [0, 0]
  correct2 = [(0,0)] * 7
else:
  hist += output.lower()+input
  opp_played.append(input)
  correct1[0] += score[predict1[0]+input]
  correct1[1] += score[predict1[1]+input]
  
  for i, p in enumerate(predict2):
    correct2[i] = ({1:correct2[i][0]+1, 0: correct2[i][0], -1: 0}[score[p+input]],  correct2[i][1]+score[p+input])

  index1 = correct1.index(max(correct1))
  index2 = correct2.index(max(correct2, key=lambda x: x[0]**3+x[1]))
  index7 = correct2[:6].index(max(correct2[:6], key=lambda x: x[0]**3+x[1]))
  predict1[1] = counter[random.choice(opp_played)]
  
  for length in range(min(10, len(hist)-2), 0, -2):
    search = hist[-length:]
    idx = hist.rfind(search, 0, -2)
    if idx != -1:
      my = hist[idx+length].upper()
      opp = hist[idx+length+1]
      predict2[0] = counter[opp]
      predict2[1] = counter[counter[my]]
      predict2[2] = counter[counter[opp]]
      predict2[3] = counter[my]
      predict2[4] = opp
      predict2[5] = my
      break
  else:
      predict2 = [random.choice(['R', 'P', 'S'])] * 7
  predict2[6] = counter[counter[predict2[index7]]]

  predict1[0] = predict2[index2]
  
  output = predict1[index1]