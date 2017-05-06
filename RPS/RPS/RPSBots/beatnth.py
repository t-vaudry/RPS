# simple bot I used for testing purposes.
# beat the move that was played n moves ago
# v2: experimenting with tuning parameters
# a little tuning can make a fairly big difference
# even on a simple bot, apparently!

import random
HISTLEN=17
DECAY=0.87
MIN_SCORE=2
NOISE_CHANCE=0.13

beat = {"R": "P", "S": "R", "P": "S"}
if input == "": # initialize variables for the first round
    output = random.choice("RPS")
    history = []
    score = [-1] * HISTLEN
    predictor = [0] * HISTLEN
else:
    history.append(input)
    if len(history) > HISTLEN:
        active = HISTLEN
    else:
        active = len(history)

    # score predictors
    best = None
    best_idx = None
    for i,p in enumerate(predictor):
        if p != 0:
            score[i] *= DECAY
            if beat[input] == p:
                score[i] += 1
            else:
                score[i] -= 1
            if best is None or score[i] > best:
                best = score[i]
                best_idx = i

    # make predictions
    for i in range(active):
        if len(history) > i:
            nth = history[-1 * (i + 1)]
            predictor[i] = beat[nth]

    if random.random() < NOISE_CHANCE:
        output = random.choice("RPS")
    elif best < MIN_SCORE:
        # fallback to randbeat
        output = beat[ random.choice(history) ]
    else:
        output = predictor[ best_idx ]