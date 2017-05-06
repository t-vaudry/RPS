import random
previous = ""
if previous == "":
      output = random.choice(["R","P","S"])
      previous = output
elif previous == "R":
      output = random.choice(["P","S"])
      previous = output
elif previous == "P":
      output = random.choice(["R","S"])
      previous = output
elif previous == "S":
      output = random.choice(["P","R"])
      previous = output