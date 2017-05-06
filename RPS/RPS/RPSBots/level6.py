import random

rps  = ["R", "P", "S", "R"]
beat1 = {"R":rps[:2], "P":rps[1:3], "S":rps[2:4]}
beat2 = {"R":rps[2:4], "P":rps[1:3], "S":rps[2:4]}

if input == "":
  output = random.choice(rps[:3])
  lin = ""
else:
  candidate = random.choice(beat1[input])
  if lin == candidate:
    candidate = random.choice(beat2[lin])
  lin = input

  #override
  if random.choice(rps[:3]) == "R":
    candidate = random.choice(beat1["R"])
  if random.choice(rps[:3]) == input:
    candidate = random.choice(beat2["R"])

  output = candidate