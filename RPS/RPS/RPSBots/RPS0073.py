import random
r = random.uniform(0, 1)
if r < 0.30:
     output = 'P'
elif r < .50:
     output = 'S'  
else:
     output = 'R'