import random, math


if input == "":
    padding = 7.0
    decay_model = 0.67
    decay_strategy = 0.95
    history = []
    weight_strategy = 1
    weight_random = 1
    prediction = ''
    my_prev = ''
    first_order = {}
    for N in ['R','P','S']:
        for O in ['R','P','S']:
            for T in ['R','P','S']:
                first_order[N+O+T] = padding
else:
    if prediction == input:
        weight_strategy += 1
    else:
        weight_random += 1
    weight_strategy *= decay_strategy
    weight_random *= decay_strategy
        
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

    pred = [x/sum(pred) for x in pred]
    pred = [math.pow(x,2) for x in pred]

    if pred[0] > pred[1] and pred[0] > pred[2]:
        prediction = 'R'
    elif pred[1] > pred[2]:
        prediction = 'P'
    else:
        prediction = 'S'

    if random.random() < weight_strategy / (weight_strategy+weight_random):
        if random.random() < pred[0] / sum(pred):
            output = "P"
        elif random.random() < pred[1] / sum(pred[1:]):
            output = "S"
        else:
            output = "R"
    else:
        output = random.choice(['R','P','S'])
else:
    output = random.choice(['R','P','S'])
my_prev = output