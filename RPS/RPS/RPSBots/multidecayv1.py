import random

if input == "":
    c_to_n = {'R':0, 'P':1, 'S':2}
    counter_move = {0:'P', 1:'S', 2:'R'}
    P = 7
    counts = [[1] * 3 for x in range(P)]
    weights = [1] * P
    decays = [0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95]
    output = random.choice(['R','P','S'])
else:
    for i in range(P):
        weights[i] += counts[i][c_to_n[input]]/sum(counts[i])
        for j in range(3):
            counts[i][j] *= decays[i]
            counts[i][c_to_n[input]] += 1
    chosen_decay = -1
    for i in range(P):
        if random.random() < weights[i]/sum(weights[i:]):
            chosen_decay = i
            break
    if chosen_decay == -1:
        chosen_decay = random.randint(0,P-1)
    chosen_prediction = -1
    for j in range(3):
         if random.random() < counts[chosen_decay][j] / sum(counts[chosen_decay][j:]):
             chosen_prediction = j
             break
    if chosen_prediction == -1:
        chosen_prediction = random.randint(0,2)
    output = counter_move[chosen_prediction]