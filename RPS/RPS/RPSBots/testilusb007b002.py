import random
if input == "":
    k = random.choice(["R","P","S"])
if k == "R":
    output = random.choice(["R","R","P","S"])
elif k == "P":
    output = random.choice(["R","P","P","S"])
elif k == "S":
    output = random.choice(["R","P","S","S"])
else:
    output = random.choice(["R","P","S"])