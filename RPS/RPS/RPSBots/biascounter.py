import random

beat = {'R':'P', 'S':'R', 'P':'S'}

def counter_bias(my_hist, ap_hist):
    r, p, s = map(my_hist.count, 'RPS')
    my_bias_count = max([r, p, s])
    my_bias_choice = 'RPS'[my_bias_count.index(my_bias_count)]
    if my_bias_count > len(my_history) / 3:
        ap_choice = beat[my_bias]
        return beat[ap_choice]
    else:
        return random.choice('RPS')

rounds = 0
my_hist = []
ap_hist = []
is_looking_for_bias = False


if rounds > 30:
    b = ap_history.count('P')
    if b > 20:
        is_looking_for_bias = True


if is_looking_for_bias:
    output = counter_bias(my_hist, ap_hist)
elif rounds > 30:
    output = random.choice('RPS')
else:
    output = 'R'


rounds += 1