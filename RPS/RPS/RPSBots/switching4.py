import random

if input == "":
  dna = ""

  anti_expected = {'P': 'S', 'S': 'R', 'R': 'P'}
  dna_encode = {'PP': '1', 'PR': '2', 'PS': '3','RP': '4','RS': '5','RR': '6','SS': '7','SP': '8','SR': '9',}
  dna_decode = {'1':'PP', '2':'PR', '3':'PS', '4':'RP', '5':'RS','6':'RR','7':'SS','8':'SP','9':'SR',}
  score = {'RR': 1, 'PP': 1, 'SS': 1,
           'PR': 2, 'RS': 2, 'SP': 2,
           'RP': 0, 'SR': 0, 'PS': 0,}
  output = random.choice(["R", "P", "S"])

  index = random.randint(0,5)
  predicted = [output] * 6
  correct = [0] * 6
else:
  dna += dna_encode[input + output]
  sc = score[output+input]

  for i in range(6):
     s = score[predicted[i]+input]
     if s == 0:
       correct[i] = 0
     elif s == 2:
       correct[i] += 1

  if sc == 0:
    m = max(correct)
    index = correct.index(m)

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
  else:
    h = random.choice(['R', 'P', 'S'])
    predicted = [h] * 6 

  output = predicted[index]