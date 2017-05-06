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
    actuallastmove = lastmove = output = random.choice(["R","P","S"])
    reverse_hist = random.randint(8,16)
    linear_decay = [ x/float(reverse_hist) for x in range(1,reverse_hist+1)]
    bail = False
    match = 0
    shift = 0
    losses = []
else:
    decay = 0.99

    if lastpair not in singles:
        singles[lastpair] = [0.0,0.0,0.0,match]
    decay_factor = pow(decay,match-singles[lastpair][3])
    singles[lastpair][3] = match
    singles[lastpair][0] *= decay_factor
    singles[lastpair][1] *= decay_factor
    singles[lastpair][2] *= decay_factor
    singles[lastpair][rpsIndex(input)] += 1.0

    if len(exchanges) > 2:
        prevtriple = tuple(exchanges[-3:])
        if prevtriple not in triples:
            triples[prevtriple] = [0.0,0.0,0.0,match]
        decay_factor = pow(decay,match-triples[prevtriple][3])
        triples[prevtriple][3] = match
        triples[prevtriple][0] *= decay_factor
        triples[prevtriple][1] *= decay_factor
        triples[prevtriple][2] *= decay_factor
        triples[prevtriple][rpsIndex(input)] += 1.0

    if len(exchanges) > 1:
        prevdouble = tuple(exchanges[-2:])
        if prevdouble not in doubles:
            doubles[prevdouble] = [0.0,0.0,0.0,match]
        decay_factor = pow(decay,match-doubles[prevdouble][3])
        doubles[prevdouble][3] = match
        doubles[prevdouble][0] *= decay_factor
        doubles[prevdouble][1] *= decay_factor
        doubles[prevdouble][2] *= decay_factor
        doubles[prevdouble][rpsIndex(input)] += 1.0

    match += 1

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

    running_check = losses[-(min(reverse_hist,len(losses))):]
    decay_len = len(running_check)
    if decay_len > 2:
        performance = sum(map( lambda x,i: x*linear_decay[i],running_check,range(0,decay_len)))
    else:
        performance = 0
    revrange = 5
    if (decay_len >= revrange and performance > 1) or (decay_len > revrange and performance >= 0.0 and running_check.count(0)/float(decay_len) > 0.5 ):
        if performance > 1:
            shift += 2
        else:
            shift += 1

        reverse_hist = random.randint(revrange,3*revrange)
        linear_decay = [ x/float(reverse_hist) for x in range(1,reverse_hist+1)]

        losses = []

    exchanges.append(lastpair)

    scores = [0,0,0]
    if len(exchanges) > 2:
        prevtriple = tuple(exchanges[-3:])
        if prevtriple in triples:
            scores[0] = triples[prevtriple][0] * 3
            scores[1] = triples[prevtriple][1] * 3
            scores[2] = triples[prevtriple][2] * 3

    if len(exchanges) > 1:
        prevdouble = tuple(exchanges[-2:])
        if prevdouble in doubles:
            scores[0] += doubles[prevdouble][0] * 2
            scores[1] += doubles[prevdouble][1] * 2
            scores[2] += doubles[prevdouble][2] * 2

    if lastpair in singles:
        scores[0] += singles[lastpair][0]
        scores[1] += singles[lastpair][1]
        scores[2] += singles[lastpair][2]

    moves = ['R','P','S']
    total = sum(scores)
    if total < 3 or scores[0] == scores[1] == scores[2]:
        lastmove = random.choice(["R","P","S"])
    else:
        r = random.randrange(0,1000)
        r = float(r)/1000.0 * total
        if r < scores[0]:
            lastmove = "P"
        elif r < scores[0]+scores[1]:
            lastmove = "S"
        else:
            lastmove = "R"

    actuallastmove = output = moves[(moves.index(lastmove) + shift)%3]