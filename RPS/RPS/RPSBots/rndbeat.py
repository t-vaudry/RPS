import random

if input == "":
  played = []
  output = random.choice(['R', 'P', 'S'])
else:
  played.append(input)
  expected = random.choice(played)
  output = {'P': 'S', 'R': 'P', 'S':'R'}[expected]