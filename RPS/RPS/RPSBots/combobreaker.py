import random

random.seed()
beat = {'R':'P','P':'S','S':'R'}
outputs = []
count = 0

if count < 10:
  output = random.choice(['R','P','S'])
elif count % 10 < 5:
  r = outputs.count('R')
  p = outputs.count('P')
  s = outputs.count('S')
  if p < r > s:
    output = beat['R']
    outputs.append('R')
  elif r < p > s:
    output = beat['P']
    outputs.append('P')
  else:
    output = beat['S']
    outputs.append('S')
else:
  output = random.choice(['R','P','S'])
  outputs.append(output)