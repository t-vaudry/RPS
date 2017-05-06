import random

a = random.random()

if(a < 0.3):
  output = "S"
elif a<0.5:
  output = "P"
else:
  output = "R"