import random

if input == "":
  random.seed()
  r = random.random()
  played = []
  output = 'S'
else:
  random.seed()
  played.append(input)
  expected = random.choice(played)
  output = {'P': 'S', 'R': 'P', 'S':'R'}[expected]

random.seed(16)