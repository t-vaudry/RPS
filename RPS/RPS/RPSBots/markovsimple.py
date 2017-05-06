import random
from collections import defaultdict

def pick_random():
    return random.choice([R, P, S])

R, P, S = "R", "P", "S"
chain_length = 3
winner = {
    R: P,
    P: S,
    S: R,
}

if not input:
    i = 0
    chain = defaultdict(lambda: defaultdict(int))
    history = []
    output = pick_random()
else:
    i += 1
    chain[tuple(history)][input] += 1
    history.append(input)
    if len(history) > 3:
        history = history[1:]
    if i < 100:
        output = pick_random()
    else:
        d = chain[tuple(history)]
        if d != {}:
            output = winner[max(d, key=lambda key: d[key])]
        else:
            output = pick_random()