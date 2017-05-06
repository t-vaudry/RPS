import random, math

def strategy(window, decay):
    longest = 0
    prediction = [1.0]*3
    for t in range(window, len(history)-1):
        if history[t-window:t] == history[-window:]:
            prediction_index = c_to_n[n_to_cc[history[t]][1]]
            prediction = [x * decay for x in prediction]
            prediction[prediction_index] += 1.0
    prediction = [x/sum(prediction) for x in prediction]
    for k in prediction:
        if k == 0:
            raise Exception('expected non-zero entries')
    return prediction

if input == "":
    history = []
    time_steps_random = 10
    cc_to_n = {'RR':0, 'RP':1, 'RS':2, 'PR':3, 'PP':4, 'PS':5, 'SR':6, 'SP':7, 'SS':8}
    n_to_cc = {0:'RR', 1:'RP', 2:'RS', 3:'PR', 4:'PP', 5:'PS', 6:'SR', 7:'SP', 8:'SS'}
    c_to_n = {'R':0, 'P':1, 'S':2}
    n_to_c = {0:'R', 1:'P', 2:'S'}
    counter_n_to_c = {0:'P', 1:'S', 2:'R'}
    n_to_score = {0:0, 1:-1, 2:1, 3:1, 4:0, 5:-1, 6:-1, 7:1, 8:0}
    T = 4
    strategy_weights = [1]*T
    prediction = [[1]*3 for T in range(T)]
    strategy_decay = 0.55
    match_decay = 1
    output = random.choice(['R','P','S'])
    max_history = 100
else:
    history.append(cc_to_n[output+input])
    while len(history) > max_history:
        history.pop(0)
    if len(history) >= time_steps_random:
        for t in range(0, T):
            strategy_weights[t] *= strategy_decay
            strategy_weights[t] += prediction[t][c_to_n[input]]
            prediction[t] = strategy(t+1, match_decay)
        chosen_predictor = prediction[strategy_weights.index(max(strategy_weights))]
        chosen_predictor = [x*x for x in chosen_predictor]
        tot = sum(chosen_predictor)
        for i in range(3):
            if random.random() < chosen_predictor[i] / tot:
                output = counter_n_to_c[i]
                break
            tot -= chosen_predictor[i]
    else:
        output = random.choice(['R','P','S'])