import random

moves = ['R', 'P', 'S']
beat_move = {'R': 'P', 'P': 'S', 'S': 'R'}

output = ''

if input == '':
    opp_history = ''
    x = -1
else:
    opp_history += input

    for length in (100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1):
        # Search for the last longest chain
        x = opp_history[:-1].rfind (opp_history[-length:])
        if x >= 0:
            # If found: Pick what will be the next move and play against it
            next_move = opp_history[x + length]
            output = beat_move[next_move]
            break

if output == '':
    output = random.choice (moves)