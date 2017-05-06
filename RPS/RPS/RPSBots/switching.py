import random

if input == "":
  dna = ""
  opp = []
  strategies = ["dna", "antidna", "opprandom"]
  actual_strategy = random.choice(strategies)
  anti_expected = {'P': 'S', 'S': 'R', 'R': 'P'}
  dna_encode = {'PP': '1', 
              'PR': '2', 
              'PS': '3',
              'RP': '4',
              'RS': '5',
              'RR': '6',
              'SS': '7',
              'SP': '8',
              'SR': '9',}
  dna_decode = {   '1':'PP', 
              '2':'PR', 
              '3':'PS',
              '4':'RP',
              '5':'RS',
              '6':'RR',
              '7':'SS',
              '8':'SP',
              '9':'SR',}
  score = {'RR': 1, 'PP': 1, 'SS': 1,
           'PR': 2, 'RS': 2, 'SP': 2,
           'RP': 0, 'SR': 0, 'PS': 0,}
  output = random.choice(["R", "P", "S"])

else:
  dna += dna_encode[input + output]
  opp.append(input)
  sc = score[output+input]
  if sc == 2:
    strategies.append(actual_strategy)
  elif sc == 1:
    strategies.append(actual_strategy)
    actual_strategy = random.choice(strategies)
  elif sc == 0:
    actual_strategy = random.choice(strategies)

  expected = random.choice(opp)

  if actual_strategy == "dna":
    for length in range(min(4, len(dna)-1), 0, -1):
      search = dna[-length:]
      idx = dna.rfind(search, 0, -1)
      if idx != -1:
        answered = dna[idx + length]
        expected = dna_decode[answered][0]
        break

  elif actual_strategy == "antidna":
    for length in range(min(4, len(dna)-1), 0, -1):
      search = dna[-length:]
      idx = dna.rfind(search, 0, -1)
      if idx != -1:
        answered = dna[idx + length]
        myexpected = dna_decode[answered][1]
        expected = anti_expected[myexpected] 
        break
  output = anti_expected[expected]