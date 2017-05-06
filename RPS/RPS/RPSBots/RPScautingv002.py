import random
RPS = ["R","P","S"]

if not input:
    output = random.choice(["R","P","S"])

else:
    if input == "R":
        RPS.append("P")
    elif input == "P":
        RPS.append("S")
    elif input == "S":
        RPS.append("R")

    output = random.choice(RPS)