import random

if input == "":
  played = []
  output = random.choice(['R', 'P', 'S'])
  strategies = ['beat', 'shift0', 'shift1', 'shift2', 'rock', 'paper', 'scissors']
  shift = {'P': 'S', 'S': 'R', 'R': 'P'}
  strategy = random.choice(strategies)
  score = {'RR': 1, 'PP': 1, 'SS': 1,
           'PR': 2, 'RS': 2, 'SP': 2,
           'RP': 0, 'SR': 0, 'PS': 0,}
else:
  played.append(input)
  
  sc = score[output+input]
  if sc == 2:
    strategies.append(strategy)
  elif sc == 1:
    strategies.append(strategy)
    strategy = random.choice(strategies)
  elif sc == 0:
    strategy = random.choice(strategies)

  if strategy == 'beat':
    expected = random.choice(played)
    output = {'P': 'S', 'R': 'P', 'S':'R'}[expected]
  elif strategy == 'shift1':
    output = shift[input]
  elif strategy == 'shift2':
    output = shift[shift[input]]
  elif strategy == 'shift0':
    output = input
  elif strategy == 'rock':
    output = 'R'
  elif strategy == 'paper':
    output = 'P'
  elif strategy == 'scissors':
    output = 'S'