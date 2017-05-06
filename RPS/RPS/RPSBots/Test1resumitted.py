#little change on rfind
#from test#1 want to know what really happen
import random

if input == "":
  dna = ""
  combine = { 'PP': '1', 
              'PR': '2', 
              'PS': '3',
              'RP': '4',
              'RS': '5',
              'RR': '6',
              'SS': '7',
              'SP': '8',
              'SR': '9',}
  split = {   '1':'PP', 
              '2':'PR', 
              '3':'PS',
              '4':'RP',
              '5':'RS',
              '6':'RR',
              '7':'SS',
              '8':'SP',
              '9':'SR',}
  anti = {'P': 'S', 'R': 'P', 'S': 'R'}
  output = random.choice(['R', 'P', 'S'])
else:
  if output != "":
    dna += combine[output + input]

  for length in range(min(25, len(dna)-1), 0, -1):
    search = dna[-length:]
    idx = dna.rfind(search, 0, -1)
    if idx != -1:
      answered = dna[idx + length]
      expected = split[answered][1]
      output = anti[expected]
      break
    else:
      output = random.choice(['R', 'P', 'S'])