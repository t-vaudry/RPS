import random

if input == "":
    rps = ['R', 'P', 'S']
    beat = {'R': 'P', 'P': 'S', 'S': 'R'}
    output = random.choice(rps)
else:
    probs = [0.95, 0.95, 0.95]
    probs[rps.index(input)] += 0.05
    probs[rps.index(beat[output])] += 0.05
    vals = map(lambda x: random.uniform(0, x), probs)
    output = beat[rps[vals.index(max(vals))]]