# See http://overview.cc/RockPaperScissors for more information about rock, paper, scissors
import random
import math
import collections

if input == "":
    rps = ['R', 'P', 'S']
    beat = {'R': 'P', 'P': 'S', 'S': 'R'}
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
    hist += input
    opplastmove = output
    mylastmove = output = random.choice(rps)
else:
    played[rps.index(input)] = 1
    for i in range(1, min(1+len(hist)/2,5)):
        patterns[hist[-i*2:]+input] += 1

    if min(played) == 1:
        if rnd - startround > 8:
            longcoupons += 1
        nocoupons += 1
        startround = rnd
        played = [0, 0, 0]

    hist += input
    probs = [1.0, 1.0, 1.0]

    for i in range(1, min(1+len(hist)/2,5)):
        probs = [p*patterns[hist[-i*2:]+h] for p,h in zip(probs,rps)]

    probs = [(p/max(probs))**0.03 for p in probs]

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