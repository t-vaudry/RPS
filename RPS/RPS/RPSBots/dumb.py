import random

r = random.random()
    
if r < 1.0/3:
   output = "R"
elif r > 1.0/3 and r < 2.0/3:
   output = "S"
elif r > 2.0/3:
   output = "P"