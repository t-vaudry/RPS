import random

MOVES = ["R","P","S"]

if not input:
    moveCounts = [0, 0, 0]
    moves = -1

moves += 1;
output = random.choice(MOVES)

if input:
    probabilities = []
    for i in moveCounts:
        probabilities.append((1 - float(i) / moves) / 2)

    r = random.random()
    sum = 0
    for i in range(0, 3):
        sum += probabilities[i]
        if r <= sum:
            output = MOVES[i]
            break

moveCounts[MOVES.index(output)] += 1