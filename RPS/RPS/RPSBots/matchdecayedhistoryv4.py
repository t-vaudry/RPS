import random, math

if input == "":
    history = []
    time_steps_random = 10
    cc_to_n = {'RR':0, 'RP':1, 'RS':2, 'PR':3, 'PP':4, 'PS':5, 'SR':6, 'SP':7, 'SS':8}
    n_to_cc = {0:'RR', 1:'RP', 2:'RS', 3:'PR', 4:'PP', 5:'PS', 6:'SR', 7:'SP', 8:'SS'}
    c_to_n = {'R':0, 'P':1, 'S':2}
    n_to_c = {0:'R', 1:'P', 2:'S'}
    n_to_score = {0:0, 1:-1, 2:1, 3:1, 4:0, 5:-1, 6:-1, 7:1, 8:0}
    match_length = 1
    decay = 0.75
else:
    history.append(cc_to_n[output+input])
if len(history) >= time_steps_random:
    prediction = strategy1()
    if random.random() < prediction[0] / sum(prediction):
        output = "P"
    elif random.random() < prediction[1] / sum(prediction[1:]):
        output = "S"
    else:
        output = "R"
else:
    output = random.choice(['R','P','S'])

def strategy1():
    longest = 0
    prediction = [1]*3
    for t in range(match_length, len(history)-1):
        if history[t-match_length:t] == history[-match_length:]:
            prediction_index = c_to_n[n_to_cc[history[t]][1]]
            prediction = [x * decay for x in prediction]
            prediction[prediction_index] += 1
    return prediction