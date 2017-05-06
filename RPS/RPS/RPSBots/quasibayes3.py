import random

CHOICES = ['R', 'P', 'S']
BEATS = {'R' : 'P', 'P' : 'S', 'S' : 'R'}
if input == "":
  output = random.choice(CHOICES)
  distribution = {'R' : {'R' : 1, 'P': 1, 'S' : 1}, 'P' : {'R' : 1, 'P': 1, 'S' : 1}, 'S' : {'R' : 1, 'P': 1, 'S' : 1}}
else:
  if output == "":
      output = random.choice(CHOICES)
  distribution[output][input] += 1
  (a, b, s) = (1,1, 'R')
  for my_strategy in CHOICES:
    opponent_strategy = BEATS[my_strategy]
    c = distribution[my_strategy][opponent_strategy]
    d = sum(distribution[my_strategy].values())
    if a * d > b * c:
      (a,b,s) = (c,d,my_strategy)
  output = s