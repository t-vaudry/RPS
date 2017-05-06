import random

if input == "":
    last = input
    throw = 0
    output = random.choice(["R","P","S"])
else:
    if throw % 2 == 0:
        throw = 1
        last = input
        output = input
    elif throw % 2 == 1:
        throw = 2