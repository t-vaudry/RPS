import random

if input == "":
    c_to_n = {'R':0, 'P':1, 'S':2}
    counter_move = {0:'P', 1:'S', 2:'R'}
    win = {'RR':1, 'RP':0, 'RS':2, 'PR':2, 'PP':1, 'PS':0, 'SR':0, 'SP':2, 'SS':1}
    P = 11
    counts = [[1] * 3 for x in range(P)]
    meta_decay = 0.9
    weight_strategy = 1
    weight_random = 1
    weights = [1] * P
    decays = [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0]
    output = random.choice(['R','P','S'])
    chosen_action = 'R'
else:
    weight_strategy *= meta_decay
    weight_random *= meta_decay
    weight_strategy += win[chosen_action+input]
    weight_random += win[input+chosen_action]
    for i in range(P):
        weights[i] *= meta_decay
        weights[i] += counts[i][c_to_n[input]]/sum(counts[i])
        for j in range(3):
            counts[i][j] *= decays[i]
            counts[i][c_to_n[input]] += 1
    chosen_decay = weights.index(max(weights))
    chosen_prediction = -1
    for j in range(3):
         if random.random() < counts[chosen_decay][j] / sum(counts[chosen_decay][j:]):
             chosen_prediction = j
             break
    if chosen_prediction == -1:
        chosen_prediction = random.randint(0,2)
    chosen_action = counter_move[chosen_prediction]
    if random.random() < weight_strategy / (weight_strategy + weight_random):
        output = chosen_action
    else:
        output = random.choice(['R','P','S'])