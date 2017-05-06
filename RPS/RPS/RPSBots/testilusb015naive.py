#enhanced naive
import random
if input == '':
  history = { 'R': 0, 'P': 0, 'S': 0 }
  output = 'R'

else:
  history[input] += 1
  _, c = min((history[c], c) for c in 'RPS')
  output = { 'R': 'P', 'P': 'S', 'S': 'R' }[c]
if output == "S":
    output = random.choice(["R","P","P","P","P","P","P","P","P","S"])
elif output == "P":
    output = random.choice(["R","R","R","R","R","R","R","R","R","P","S"])
elif output == "R":
    output = random.choice(["R","P","S","S","S","S","S","S","S"])