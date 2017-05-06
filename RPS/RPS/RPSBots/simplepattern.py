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
    lastmove = output = random.choice(["R","P","S"])
else:
    decay = 0.2

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
    exchanges.append(lastpair)
    
    scores = [0,0,0]
    if len(exchanges) > 2:
        prevtriple = tuple(exchanges[-3:])
        if prevtriple in triples:
            scores[0] = triples[prevtriple][0] * 6
            scores[1] = triples[prevtriple][1] * 6
            scores[2] = triples[prevtriple][2] * 6
    
    if len(exchanges) > 1:
        prevdouble = tuple(exchanges[-2:])
        if prevdouble in doubles:
            scores[0] += doubles[prevdouble][0] * 3
            scores[1] += doubles[prevdouble][1] * 3
            scores[2] += doubles[prevdouble][2] * 3
    
    if lastpair in singles:
        scores[0] += singles[lastpair][0]
        scores[1] += singles[lastpair][1]
        scores[2] += singles[lastpair][2]
    
    if scores[0] > scores[1] and scores[0] > scores[2]:
        output = "R"
    elif scores[1] > scores[0] and scores[1] > scores[2]:
        output = "P"
    else:
        output = "S"
    lastmove = output