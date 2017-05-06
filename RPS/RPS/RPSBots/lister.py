import random
moves = {'R': 'P', 'P': 'S', 'S': 'R'}
if not input:
    i = 0
    history = ''
    my_moves = ''
    things = []
    output = random.choice(moves.keys())
else:
    i += 1
    history += input
    my_moves += output

    things += i*list(input)
    things += i*list(moves[output])

    their_move = random.choice(things)
    output = moves[their_move]