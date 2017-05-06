import random
if input == "R":
    output = random.choice(["P","S"])
elif input == "P":
    output = random.choice(["R","S"])
else:
    output = random.choice(["R","P"])