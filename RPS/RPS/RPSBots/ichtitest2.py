import random


if input == "":
    opponentPlays = []
    myPlays = []
    o = random.choice(["R", "P", "S"])
    myPlays.append(o)
    output = o
else:
    opponentPlays.append(input)
    print len(opponentPlays)
    if (len(opponentPlays) < 3):
        o = random.choice(["R", "P", "S"])
        myPlays.append(o)
        output = o
    else:
        
        o = random.choice(["R", "S", "S"])
        myPlays.append(o)
        output = o