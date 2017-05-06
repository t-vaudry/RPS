import random


beat = {'R':'P', 'S':'R', 'P':'S'}

def counter_bias(my_hist, ap_hist):
    my_counts = map(my_hist.count, 'RPS')
    my_bias_count = max(my_counts)
    my_bias_choice = 'RPS'[my_counts.index(my_bias_count)]
    if my_bias_count > len(my_hist) / 3:
        ap_choice = beat[my_bias_choice]
        return beat[ap_choice]
    else:
        return random.choice('RPS')


# first round; var initialization
if input == '':
    my_hist = ''
    ap_hist = ''
    rounds = 0
    is_looking_for_bias = False


ap_hist += input
if rounds > 30:
    b = ap_hist.count('P')
    if b > 20:
        is_looking_for_bias = True


if is_looking_for_bias:
    output = counter_bias(my_hist, ap_hist)
elif rounds > 30:
    output = random.choice('RPS')
else:
    output = 'R'


my_hist += output
rounds += 1