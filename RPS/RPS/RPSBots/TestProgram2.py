import random
if input ==  "":
    output = "R"
    n = 0
elif input == "P":
    output = random.choice(["R","P","S"])
elif input == "S":
    output = "SPPSP"
    output = random.choice(["R","P","S"])
elif input == "R":
    output = random.choice(["R","P","S"])