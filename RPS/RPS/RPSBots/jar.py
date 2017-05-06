import random

if input == "R":
    output = random.choice(["R","P"])

if input == "P":
    output = random.choice(["P","S"])

if input == "S":
    output = random.choice(["S","R"])

else:
    output = "R"