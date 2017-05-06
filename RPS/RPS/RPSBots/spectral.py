import random

if input == "":
  spec = [None] *14
  strats = [(2,0), (2,1), (3,0), (3,1), (3,2), (4,0), (4,1), (4,2), (4,3), (5,0), (5,1), (5,2), (5,3), (5,4)]
  round = 1
  canditates = [None] * len(strats)
  correct = [0] * len(strats)
  output = random.choice(['R', 'P', 'S'])
  score = {'RR': 0, 'PP': 0, 'SS': 0,
           'PR': 1, 'RS': 1, 'SP': 1,
           'RP': -1, 'SR': -1, 'PS': -1,}
  counter = {'P': 'S', 'S': 'R', 'R': 'P'}
  index = random.randint(0, len(strats)-1)
else:
  for i,c in enumerate(canditates):
    if c is None:
      continue
    sc = score[c+input]
    if sc == 1:
      correct[i] += 1
    if sc == -1:
      correct[i] = 0
 
  for i, (j,k) in enumerate(strats):
    if round % j == k:
       canditates[i] = counter[output] 
  
  possible_strats = [i for i, (a, b) in enumerate(strats) if round % a == b]
  round += 1
  best_correct = max([correct[i] for i in possible_strats])
  best_indices = [i for i in possible_strats if best_correct == correct[i]]
  best_index = random.choice(best_indices)
  b = canditates[best_index]
  if b == None:
    output = random.choice(['R','P', 'S'])
  else:
    output = b