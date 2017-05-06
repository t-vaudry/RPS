import random
if input:
    output = {'R' : 'P',
              'P' : 'S',
              'S' : 'R'}[last]
    last = input
else:
    output = random.choice(["R","P","S"])
    last = random.choice(["R","P","S"])