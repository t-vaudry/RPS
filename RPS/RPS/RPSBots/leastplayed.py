import random

if input == '':
  history = { 'R': 0, 'P': 0, 'S': 0 }
  output = random.choice(['R', 'P', 'S'])

else:
  history[input] += 1
  c, _ = sorted((k, v) for k, v in history.items())[0]
  output = { 'R': 'P', 'P': 'S', 'S': 'R' }[c]