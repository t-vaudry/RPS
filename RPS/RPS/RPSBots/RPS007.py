import random
r = random.uniform(0, 1)
if r < 0.25:
     output = 'R'
elif r < .5:
     output = 'S'  
else:
     output = 'P'