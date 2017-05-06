import random
moves = {'R': 'P', 'P': 'S', 'S': 'R'}

if len(input) < 25:
    output = random.choice(moves.keys())
else:
    possible = [moves[i] for i in input]
    output = random.choice(possible)