import random

if input == "":
  output = "S"
algo = random.choice(["a", "b", "c"])
if  algo == "a":
  # Play randomly.
  output = random.choice(["S", "R", "P"])
elif algo == "b":
  # Play the move that would have won last time.
  if input == "R":
    output = "P"
  elif input == "P":
    output = "S"
  else:
    output = "R"
elif algo == "c":
  # Play the same move again.
    output = output