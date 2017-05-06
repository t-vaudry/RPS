import random

if input == "R":
    output = random.choice(["R","P"])
elif input == "P":
    output = random.choice(["P","S"])
elif input == "S":
    output = random.choice(["S","R"])
else:
    output = "R"