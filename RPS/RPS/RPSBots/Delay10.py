import random

if input == "":
  output = random.choice(("R", "P", "S"))
  timer = ""
else:
  timer += input
  if len(timer) >= 10:
    output = timer[-10]
  else:
    output = random.choice(("R", "P", "S"))