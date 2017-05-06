import random
m = {'R': 'P', 'P': 'S', 'S': 'R'}
if input != '':
     if random.uniform(0, 1) > .5:
          output = m[input]
     else:
          del m[input]
          output = random.choice(m.values())
else:
     output = 'R'