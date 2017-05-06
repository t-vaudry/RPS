import random
trump = {'R': 'P', 'P': 'S', 'S': 'R'}
hist = ""

def get_move(hist):
    for k in range(len(hist)-1, 1, -1):
        m = hist.rfind(hist[-k:], 0, -1)
        if m != -1 : 
            return trump[hist[m+k]]
    return random.choice('RPS')

hist += input
output = get_move(hist)