import random

def randPlay():
    return random.choice(["R","P","S"])

def beats(x):
    if x == "R":
        return "P"
    elif x == "P":
        return "S"
    elif x == "S":
        return "R"
    else:
        return randPlay()

output = randPlay()