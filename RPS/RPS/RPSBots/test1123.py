import random

if input == "":
  output = random.choice(["R","P","S"])
else:
  whatif = random.randint(0,1)
  if whatif == 1:
    output = random.choice(["R","P","S"])
  else:
    output = input