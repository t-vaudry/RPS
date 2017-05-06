# Extend switching7: Also look only at opponent/mymoves
import random

if input == "":
  hist = ""
  opp_hist = ""
  my_hist = ""
  opp_played = []
  counter = {'P': 'S', 'S': 'R', 'R': 'P'}
  score = {'RR': 0, 'PP': 0, 'SS': 0, 'PR': 1, 'RS': 1, 'SP': 1,'RP': -1, 'SR': -1, 'PS': -1,}
  output = random.choice(["R", "P", "S"])

  predict1 = [output, output]
  predict2 = [output] * 18
  correct1 = [0, 0]
  correct2 = [(0,0)] * len(predict2)
else:
  hist += output.lower()+input
  opp_hist += input
  my_hist += output
  opp_played.append(input)
  correct1[0] += score[predict1[0]+input]
  correct1[1] += score[predict1[1]+input]
  
  for i, p in enumerate(predict2):
    correct2[i] = ({1:correct2[i][0]+1, 0: correct2[i][0], -1: 0}[score[p+input]],  correct2[i][1]+score[p+input])

  index1 = correct1.index(max(correct1))
  index2 = correct2.index(max(correct2))

  predict1[1] = counter[random.choice(opp_played)]
  rh = random.choice(["R", "P", "S"])  

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
    for i in range(6):
      predict2[i] = rh

  for length in range(min(5, len(opp_hist)-1), -1):
    opp_search = opp_hist[-length]
    idx = opp_hist.rfind(opp_search, 0, -1)
    if idx != -1:
      my = my_hist[idx+length]
      opp = opp_hist[idx+length]
      predict2[6] = counter[opp]
      predict2[7] = counter[counter[my]]
      predict2[8] = counter[counter[opp]]
      predict2[9] = counter[my]
      predict2[10] = opp
      predict2[11] = my
      break
  else:
    for i in range(6,12):
      predict2[i] = rh

  for length in range(min(5, len(my_hist)-1), -1):
    my_search = my_hist[-length:]
    idx = my_hist.rfind(my_search, 0, -1)
    if idx != -1:
       my = my_hist[idx+length]
       opp = opp_hist[idx+length]
       predict2[12] = counter[opp]
       predict2[13] = counter[counter[my]]
       predict2[14] = counter[counter[opp]]
       predict2[15] = counter[my]
       predict2[16] = opp
       predict2[17] = my
       break
  else:
    for i in range(12,18):
      predict2[i] = rh

  predict1[0] = predict2[index2]

  output = predict1[index1]