from random import *
from math import *

if input == "":
    c_to_n = {'R':0, 'P':1, 'S':2}
    cc_to_m = {'rR':0, 'rP':1, 'rS':2,
               'pR':3, 'pP':4, 'pS':5,
               'sR':6, 'sP':7, 'sS':8}
    win_set  = ['rP', 'pS', 'sR']
    draw_set = ['rR', 'pP', 'sS']
    lose_set = ['rS', 'pR', 'sP']
    shift = {'r':'s', 'p':'r', 's':'p'}
    response = {'r':'P', 'p':'S', 's':'R'}
    random_moves = 10
    decay = 0.85
    weight_random = 1
    weight_0th_order = 1
    weight_1st_order = 1
    weight_2nd_order = 1
    prediction_0th_order = choice(['r','p','s'])
    prediction_1st_order = choice(['r','p','s'])
    prediction_2nd_order = choice(['r','p','s'])
    output = choice(['R','P','S'])
    history = ''
    max_match_length = 4
    losing_streak = 0
    max_losing_streak = 7
    intentional_move = False
else:
    history += input.lower() + output

    if (input.lower() + output) in lose_set and intentional_move:
        losing_streak += 1
        if losing_streak >= max_losing_streak:
            weight_random = 5
            weight_0th_order = 5
            weight_1st_order = 5
            weight_2nd_order = 5
            losing_streak = 0
    if len(history) > random_moves:
        weight_random *= decay
        weight_0th_order *= decay
        weight_1st_order *= decay
        weight_2nd_order *= decay
        if prediction_0th_order == input.lower():
            weight_0th_order += 1
        elif prediction_1st_order == input.lower():
            weight_1st_order += 1
        else:
            weight_2nd_order += 1
        if (input.lower() + output) not in win_set:
            weight_random += 1
        suffix = ''
        for d in range(max_match_length, 0, -1):
            prefix = history[-d*2:]
            i = history[:-2].rfind(prefix) #[:-2] so as not to match current
            if i > -1:
                suffix = history[i + d*2]
                break
        if suffix != '':
            assert suffix in ['r','p','s']
            prediction_0th_order = suffix
            prediction_1st_order = shift[suffix]
            prediction_2nd_order = shift[shift[suffix]]
        else:
            prediction_0th_order = choice(['r','p','s'])
            prediction_1st_order = choice(['r','p','s'])
            prediction_2nd_order = choice(['r','p','s'])
        weights = [weight_0th_order, weight_1st_order, weight_2nd_order, weight_random]
        weights = [x/sum(weights) for x in weights]
        intentional_move = True
        if random() < weights[0] / sum(weights):
            output = response[prediction_0th_order]
        elif random() < weights[1] / sum(weights[1:]):
            output = response[prediction_1st_order]
        elif random() < weights[2] / sum(weights[2:]):
            output = response[prediction_2nd_order]
        else:
            intentional_move = False
            output = choice(['R','P','S'])
    else:
        output = choice(['R','P','S'])