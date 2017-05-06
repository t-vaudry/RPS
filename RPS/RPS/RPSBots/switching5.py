# Also uses rndbeat as an available strategy like switching3.
# Use total to avoid drawing strategies when behind.
import random

if input == "":
  dna = ""
  opp_played = []
  anti_expected = {'P': 'S', 'S': 'R', 'R': 'P'}
  dna_encode = {'PP': '1', 'PR': '2', 'PS': '3','RP': '4','RS': '5','RR': '6','SS': '7','SP': '8','SR': '9',}
  dna_decode = {'1':'PP', '2':'PR', '3':'PS', '4':'RP', '5':'RS','6':'RR','7':'SS','8':'SP','9':'SR',}
  score = {'RR': 0, 'PP': 0, 'SS': 0,
           'PR': 1, 'RS': 1, 'SP': 1,
           'RP': -1, 'SR': -1, 'PS': -1,}
  total = 0
  output = random.choice(["R", "P", "S"])

  index = random.randint(0,5)
  predicted = [output] * 7
  correct = [0] * 7
else:
  dna += dna_encode[input + output]
  opp_played.append(input)
  sc = score[output+input]
  total += sc

  for i, p in enumerate(predicted):
     s = score[p+input]
     if s == -1:
       correct[i] = 0
     elif s == 1:
       correct[i] += 1

  if sc == -1 or (total <= 0 and sc == 0):
    m = max(correct)
    index = correct.index(m)

  c = anti_expected[random.choice(opp_played)]
  for i, p in enumerate(predicted):
    predicted[i] = c
  
  answered = None
  for length in range(min(4, len(dna)-1), 0, -1):
    search = dna[-length:]
    idx = dna.rfind(search, 0, -1)
    if idx != -1:
      answered = dna_decode[dna[idx + length]]
      my = answered[1]
      opp = answered[0]
      predicted[0] = my
      predicted[1] = anti_expected[my]
      predicted[2] = anti_expected[anti_expected[my]]
      predicted[3] = opp
      predicted[4] = anti_expected[opp]
      predicted[5] = anti_expected[anti_expected[opp]]
      break

  output = predicted[index]