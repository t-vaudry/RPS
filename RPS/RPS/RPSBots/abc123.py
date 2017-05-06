from random import randrange

def bias(history):
    r = 0
    p = 0
    s = 0
    for move in history:
        if move == 'R':
            r += 1
        elif move == 'P':
            p += 1
        else:
            s += 1
    if s > p and s > r:
        return 'S', (float(s) / (s+p+r)) * 100
    elif p > r and p > s:
        return 'P', (float(p) / (s+p+r)) * 100
    elif r > p and r > s:
        return 'R', (float(r) / (s+p+r)) * 100
    else:
        return None

def best(input):
    moves = ['R', 'P', 'S']
    move = bias(input)
    if not move:
        return moves[randrange(3)]
    return move[0]

output = best(input)