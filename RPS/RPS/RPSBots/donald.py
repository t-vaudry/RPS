import random

def get_move(hist):
    n = min(20, len(hist)-1)
    for k in range(n, 1, -1):
        m = hist.rfind(hist[-k:], 0, -1)
        if m != -1 :
            return trump[hist[m+k]]
    return random.choice('RPS')

if input == "":
    trump = {'R': 'P', 'P': 'S', 'S': 'R'}
    hist = ''
    output =  random.choice('RPS')
else:
    hist += input
    output = get_move(hist)