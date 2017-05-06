# my first attempt for the RPScontest, and the first time every using python
# trying to return a weighted random choice based on the history

import random

if input == "":
  r = p = s = 10
elif input == "R":
  r += 1
elif input == "P":
  p += 1
elif input == "S":
  s += 1

ra = ["R"] * s
pa = ["P"] * r
sa = ["S"] * p

if input == "":
  output = random.choice(["R","P","S"])
else:
  output = random.choice(ra + pa + sa)