import random
moves = {'R': 'P', 'P': 'S', 'S': 'R'}
if not input:
    history = ''
history += input

if len(history) < 25:
    output = random.choice(moves.keys())
else:
    possible = [moves[i] for i in history[-25:]]
    output = random.choice(possible)