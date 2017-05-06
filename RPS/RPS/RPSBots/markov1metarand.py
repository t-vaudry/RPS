import random

#meta random

if not input:
    beat={'R':'P','P':'S','S':'R'}
    output = random.choice(['R','P','S'])
    successes = [0,0,0,0,0,0]
    turn = 0
else:
    turn += 1
    if turn > 1:
        for i in range(len(predictions)):
            if predictions[i] is input:
                successes[i] += 1#successes[i] = (successes[i]+1)/2.0
    predictions = [output,beat[output],beat[beat[output]],input,beat[input],beat[beat[input]]]

    if turn <= 1:
        output = random.choice(['R','P','S'])
    else:
        succ_sum = 0
        for i in range(len(successes)):
            succ_sum += successes[i]
        r = random.uniform(0,succ_sum)
        output_idx = 0
        for i in range(len(successes)):
            r -= successes[i]
            if r < 0:
                output_idx = i
                break
        output = beat[predictions[output_idx]]

last_input = input
last_output = output