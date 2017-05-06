import random

def rpsIndex(val):
    if val == "R":
        return 0
    elif val == "P":
        return 1
    return 2

if input == "":
    lastpair = ("","")
    exchanges = []
    singles = {}
    doubles = {}
    triples = {}
    output = random.choice(["R","P","S"])
    reverse = False
    reverse_hist = random.randint(8,16)
    losses = []
    lastmove = actuallastmove = ""
else:
    decay = 0.50

    if lastpair not in singles:
        singles[lastpair] = [1.0,1.0,1.0]
    singles[lastpair][0] *= decay
    singles[lastpair][1] *= decay
    singles[lastpair][2] *= decay
    singles[lastpair][rpsIndex(input)] += 1.0

    if len(exchanges) > 2:
        prevtriple = tuple(exchanges[-3:])
        if prevtriple not in triples:
            triples[prevtriple] = [1.0,1.0,1.0]
        triples[prevtriple][0] *= decay
        triples[prevtriple][1] *= decay
        triples[prevtriple][2] *= decay
        triples[prevtriple][rpsIndex(input)] += 1.0

    if len(exchanges) > 1:
        prevdouble = tuple(exchanges[-2:])
        if prevdouble not in doubles:
            doubles[prevdouble] = [1.0,1.0,1.0]
        doubles[prevdouble][0] *= decay
        doubles[prevdouble][1] *= decay
        doubles[prevdouble][2] *= decay
        doubles[prevdouble][rpsIndex(input)] += 1.0

    lastpair = (lastmove,input)

    losses.append(0)
    if actuallastmove == "R":
        if input == "P":
            losses[-1] = 1
        elif input == "S":
            losses[-1] = -1
    elif actuallastmove == "P":
        if input == "S":
            losses[-1] = 1
        elif input == "R":
            losses[-1] = -1
    elif actuallastmove == "S":
        if input == "R":
            losses[-1] = 1
        elif input == "P":
            losses[-1] = -1


    if len(losses) >= reverse_hist and sum(losses[-reverse_hist:]) > 0:
        reverse = not reverse
        reverse_hist = random.randint(8,16)
        losses = []

    exchanges.append(lastpair)

    scores = [0,0,0]
    if len(exchanges) > 2:
        prevtriple = tuple(exchanges[-3:])
        if prevtriple in triples:
            scores[0] = triples[prevtriple][0] * 12
            scores[1] = triples[prevtriple][1] * 12
            scores[2] = triples[prevtriple][2] * 12

    if len(exchanges) > 1:
        prevdouble = tuple(exchanges[-2:])
        if prevdouble in doubles:
            scores[0] += doubles[prevdouble][0] * 5
            scores[1] += doubles[prevdouble][1] * 5
            scores[2] += doubles[prevdouble][2] * 5

    if lastpair in singles:
        scores[0] += singles[lastpair][0]
        scores[1] += singles[lastpair][1]
        scores[2] += singles[lastpair][2]

    if scores[0] > scores[1] and scores[0] > scores[2]:
        if reverse:
            output = "R"
            lastmove = "P"
        else:
            lastmove = output = "P"
    elif scores[1] > scores[0] and scores[1] > scores[2]:
        if reverse:
            output = "P"
            lastmove = "S"
        else:
            lastmove = output = "S"
    else:
        if reverse:
            output = "S"
            lastmove = "R"
        else:
            lastmove = output = "R"
    actuallastmove = output