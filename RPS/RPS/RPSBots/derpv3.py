import random, math

if input == "":
    padding = 7.0
    decay_model = 0.75
    history = []
    my_prev = ''
    first_order = {}
    for i in ['R','P','S']:
        for j in ['R','P','S']:
            for k in ['R','P','S']:
                first_order[i+j+k] = padding
else:
    your_prev = input
    history.append((my_prev, your_prev))
if len(history) >= 2:
    pred = [1,1,1]
    pred[0] = first_order[my_prev + your_prev + 'R']
    pred[1] = first_order[my_prev + your_prev + 'P']
    pred[2] = first_order[my_prev + your_prev + 'S']
    first_order[history[-2][0] + history[-2][1] + history[-1][1]] += 1
    first_order[my_prev + your_prev + 'R'] *= decay_model
    first_order[my_prev + your_prev + 'P'] *= decay_model
    first_order[my_prev + your_prev + 'S'] *= decay_model

    pred = [math.pow(x,2) for x in pred]
    
    if random.random() < pred[0] / sum(pred):
        output = "P"
    elif random.random() < pred[1] / sum(pred[1:]):
        output = "S"
    else:
        output = "R"
else:
    output = random.choice(['R','P','S'])
my_prev = output