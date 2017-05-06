# See http://overview.cc/RockPaperScissors for more information about rock, paper, scissors
import random
import math
import collections

if input == "":
    rps = ['R', 'P', 'S']
    beat = {'R': 'P', 'P': 'S', 'S': 'R'}
    cede = {'R': 'S', 'P': 'R', 'S': 'P'}
    hist = ""
    output = random.choice(rps)
    patterns = collections.defaultdict(lambda: 10)
    rnd = .0
    startround = repeated = countered = 0
    played = [0, 0, 0]
    nocoupons = 1
    longcoupons = 1.0
    hist = ""
elif rnd == 0:
    rnd += 1.1
    myplayed = [int(e==output) for e in rps]
    hist += output + input
    opplastmove = output
    mymost = [output]
    mmycounter = 0
    againstmymostplayed = [0, 1.0]
    mylastmove = output = random.choice(rps)
    test = [0, 0]
else:
    if againstmymostplayed[0]/againstmymostplayed[1] > 0.345:
        test[int(beat[output]==input)] += 1

    mostplayedlist = random.choice([rps[i] for i, e in enumerate(myplayed) if e == max(myplayed)])
    decay = 0.5 
    againstmymostplayed = [(againstmymostplayed[0] + 0.01*(0.333333-(againstmymostplayed[1] - againstmymostplayed[0])/againstmymostplayed[1]) + 1.0*int(cede[input] in mostplayedlist)/len(mostplayedlist)), (againstmymostplayed[1]+1)]
    myplayed[rps.index(output)] += 1

    if cede[input] in mymost:
        mmycounter += 1
    played[rps.index(input)] = 1
    for i in range(1, min(1+len(hist)/2,5)):
        patterns[hist[-i*2:]+input] += 1
        patterns[hist[-i*2:]+output.lower()] += 1

    if min(played) == 1:
        if rnd - startround > 8:
            longcoupons += 1
        nocoupons += 1
        startround = rnd
        played = [0, 0, 0]

    hist += output + input
    probs = [1.0, 1.0, 1.0]

    myprobs = [1.0, 1.0, 1.0]
    for i in range(1, min(1+len(hist)/2,5)):
        probs = [p*patterns[hist[-i*2:]+h] for p,h in zip(probs,rps)]

    for i in range(min(1+len(hist)/2,6),0, -1):
        tmp = [patterns[hist[-i*2:]+h.lower()] for h in rps]
        if sum(tmp) > 30:
            myprobs = tmp
            break

    mymost = [e for e, p in zip(rps, myprobs) if p == max(myprobs)]
    probs = [(p/max(probs))**0.03 for p in probs]

    if mmycounter/rnd > 0.41:
        for e in mymost:
            probs[rps.index(beat[e])] += .01/(1.41-(mmycounter/rnd))**6

    if againstmymostplayed[0]/ againstmymostplayed[1] > 0.345:
        for j in [h for h, k in zip(rps, myplayed) if k == max(myplayed)]:
            probs[rps.index(beat[j])] += 0.33-againstmymostplayed[0]/ againstmymostplayed[1]

    if rnd - startround > 8 and longcoupons/nocoupons > 0.117 and sum(played)==2:
       probs[played.index(0)] -= 2*longcoupons/nocoupons 
    if opplastmove == input:
        repeated += 1
    if beat[mylastmove] == input:
        countered += 1
    if repeated / rnd > 0.3:
        probs[rps.index(input)] += 0.01 / (0.999-repeated/rnd)**2
    if countered / rnd > 0.33:
        probs[rps.index(beat[output])] += 0.01 / (0.999- countered/rnd)**2
    vals = map(lambda x: random.uniform(0, x), probs)
    opplastmove = input
    mylastmove = output
    output = beat[rps[vals.index(max(vals))]]
    rnd += 1