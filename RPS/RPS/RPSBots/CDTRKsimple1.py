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

if not input: # initialize variables for the first round
    oppMoves = ""
    output = randPlay()
    myMoves = output
else:
    oppMoves += input
    
    if len(myMoves) <= 1:
        output = beats(beats(oppMoves[0]))
        myMoves += output
    elif oppMoves[-1] == beats(myMoves[-1]) and oppMoves[-2] == beats(myMoves[-2]):
        output = randPlay()
        myMoves +=output
    elif oppMoves[-1] == oppMoves[-2]:
        output = beats(oppMoves[-1])
        myMoves +=output