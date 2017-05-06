import random

moves = ['R', 'P', 'S']
beat_move = {'R': 'P', 'P': 'S', 'S': 'R'}

def biaised_rps (R, P, S):
    """ Play R, P or S in fonction of their frequencies """
    # biaised_rps (1, 1, 1) play 33% R, 33% P and 33% S
    # biaised_rps (2, 1, 0) play 66% R, 33% P and  0% S

    x = random.random()
    if x < R / float (R + P + S):
        return 'R'
    elif x < (R + P) / float (R + P + S):
        return 'P'
    else:
        return 'S'


output = ''

if input == '':
    opp_history = ''

else:
    opp_history += input

    for length in (100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1):
        # Search for the last longest chain
        M = {'R': 0, 'P': 0, 'S': 0}
        x = 0
        while True:
            p = opp_history[x:-1].find (opp_history[-length:])
            if p == -1:
                break
            x += p
            M[opp_history[x + length]] += 1
            x += 1

        # If found: Pick what will be probably the next move and play against it
        if x != 0:
            next_move = biaised_rps (M['R'], M['P'], M['S'])
            output = beat_move[next_move]
            break

if output == '':
    output = random.choice (moves)