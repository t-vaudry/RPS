if input == '':
  history = { 'R': 0, 'P': 0, 'S': 0 }
  output = 'R'

else:
  history[input] += 1
  _, c = min((history[c], c) for c in 'RPS')
  output = { 'R': 'P', 'P': 'S', 'S': 'R' }[c]