import random

opponentPlays = []
myPlays = []
if input == "":
    o = random.choice(["R", "P", "S"])
    myPlays.append(o)
    output = o
else:
    opponentPlays.append(input)
    if (len(opponentPlays) < 3):
        o = random.choice(["R", "P", "S"])
        myPlays.append(o)
        output = o
    else:
        
        o = random.choice(["R", "S", "S"])
        myPlays.append(o)
        output = o