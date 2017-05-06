import random

if input:
 choices += beats[input]
else:
 beats = {'R': 'P', 'P': 'S', 'S': 'R'}
 choices = 'RPS'
output = random.choice(choices)