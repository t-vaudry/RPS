# Similar to switching3, but a different strategy selection:
# always use best performed strategy

import random

if input == "":
  dna = ""
  opp = []

  anti_expected = {'P': 'S', 'S': 'R', 'R': 'P'}
  dna_encode = {'PP': '1', 'PR': '2', 'PS': '3', 'RP': '4', 'RS': '5','RR': '6','SS': '7','SP': '8', 'SR': '9',}
  dna_decode = {'1':'PP', '2':'PR', '3':'PS','4':'RP','5':'RS','6':'RR','7':'SS','8':'SP','9':'SR',}
  score = {'RR': 0, 'PP': 0, 'SS': 0, 'PR': 1, 'RS': 1, 'SP': 1,'RP': -1, 'SR': -1, 'PS': -1,}
  output = random.choice(["R", "P", "S"])

  index = random.randint(0,2)
  candidates = [output] * 3
  performance = [0, 0, 0]
  total = 0
else:
  dna += dna_encode[input + output]
  opp.append(input)
  sc = score[output+input]
  total += sc

  for i in range(3):
     s = score[candidates[i]+input]
     if s == -1:
       performance[i] = 0
     elif s == 1:
       performance[i] += 1
     elif total < 0 and s == 0:
       performance[i] = 0

  m = max(performance)
  bestlist = [i for i, c in enumerate(performance) if c == m] 
  index = random.choice(bestlist)

  candidates[0] = anti_expected[random.choice(opp)]
  candidates[1] = anti_expected[random.choice(opp)]
  candidates[2] = anti_expected[random.choice(opp)]

  for length in range(min(4, len(dna)-1), 0, -1):
    search = dna[-length:]
    idx = dna.rfind(search, 0, -1)
    if idx != -1:
      answered = dna_decode[dna[idx + length]]
      candidates[1] = anti_expected[answered[0]]
      candidates[2] = anti_expected[anti_expected[answered[1]]]
      break

  output = candidates[index]