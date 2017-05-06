import random
winners = {'P': 'S', 'R': 'P', 'S': 'R'}
if input == '':
    i = 0
    myMoves = ''
    moves= []
    output = 'R'
else:
    i += 1
    myMoves += output

    moves += i*list(input)
    moves += i*list(winners[output])

    theirMove = random.choice(moves)
    output = winners[theirMove]