import random

if not input or len(prev_output) < 2:
    output = 'RPS'[random.randrange(3)]

    if not input:
        prev_output = []
else:
    opponent_rotation = ('RPS'.index(input) - 'RPS'.index(prev_output[-2])) % 3
    output = 'RPS'[('RPS'.index(prev_output[-1]) + opponent_rotation + 1) % 3]

prev_output.append(output)