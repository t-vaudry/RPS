import random
r = random.uniform(0, 1)
if r < 0.33:
     output = 'P'
elif r < .66:
     output = 'S'  
else:
     output = 'R'