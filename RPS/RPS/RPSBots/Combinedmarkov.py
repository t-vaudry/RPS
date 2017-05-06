# Adapted from another entry, forgot which one.
import random

moves = ['R', 'P', 'S']
dna_encode = {
    'PP': '1', 'PR': '2', 'PS': '3',
    'RP': '4', 'RS': '5', 'RR': '6',
    'SS': '7', 'SP': '8', 'SR': '9' }
beat_move = {'R': 'P', 'P': 'S', 'S': 'R'}

if input == '':
    opp_history = ''
    dna = ''
    output = ''
else:
    opp_history += input
    dna += dna_encode[input + output]

    for length in (100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1):
        # Search for the last longest chain
        x = dna[:-1].rfind (dna[-length:])
        if x >= 0:
            # If found: Pick what will be the next move and play against it
            next_move = opp_history[x + length]
            output = beat_move[next_move]
            break

if output == '':
    output = random.choice (moves)