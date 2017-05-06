def cycle(move):
    if move == 'R': return 'P'
    if move == 'P': return 'S'
    if move == 'S': return 'R'


def window_equal(w1_start, w2_start, s):
    for i in range(s):
        if history[w1_start+i] != history[w2_start+i]:
            return False
    return True

def predict_move(window_size):
    s = window_size
    # history has to be at least s + s + 1 in length to find a match plus next
    # move
    L = len(history)

    if L < s + s + 1: return None

    match_window_start = L - s
    window_start = L - s - s - 1
    while window_start >= 0:
        if window_equal(window_start, match_window_start, s):
            return history[window_start+s]
        window_start -= 1

def go():
    global output
    history.append(input)
    move = predict_move(5)
    if move:
        output = cycle(move)
    else:
        output = 'P'

if input == '':
    history = []
    output = 'P'
else:
    go()