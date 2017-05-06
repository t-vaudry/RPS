import random
if input == "":
    output = random.choice(["R","P","S"])
if input == "R":
    output = random.choice(["P","S"])
elif input == "P":
    output = random.choice(["R","S"])
elif input == "S":
    output = random.choice(["R","P"])
else:
    output = random.choice(["R","P","S"])