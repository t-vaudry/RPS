import random
if input == "":
    pad = 1.0
    decay0 = 0.9
    decay1 = 0.7
    decay2 = 0.5
    model0 = {'R':pad, 'P':pad, 'S':pad}
    model1 = {}
    model2 = {}
    history = []
else:
    history.append((output, input))
    
if len(history) >= 3:
    prediction0 = [1] * 3
    prediction1 = [1] * 3
    prediction2 = [1] * 3
    prefix1 = history[-2][0]+history[-2][1]
    prefix2 = history[-3][0]+history[-3][1]+history[-2][0]+history[-2][1]
    actual_suffix = input
    for k in ['R','P','S']:
        if model1.get(prefix1 + k) == None:
            model1[prefix1 + k] = pad
        if model2.get(prefix2 + k) == None:
            model2[prefix2 + k] = pad
            
    prediction0[0] = model0['R']
    prediction0[1] = model0['P']
    prediction0[2] = model0['S']
    model0[actual_suffix] += 1
    model0['R'] *= decay0
    model0['P'] *= decay0
    model0['S'] *= decay0

    prediction1[0] = model1[prefix1 + 'R']
    prediction1[1] = model1[prefix1 + 'P']
    prediction1[2] = model1[prefix1 + 'S']
    model1[prefix1 + actual_suffix] += 1
    model1[prefix1 + 'R'] *= decay1
    model1[prefix1 + 'P'] *= decay1
    model1[prefix1 + 'S'] *= decay1

    prediction2[0] = model2[prefix2 + 'R']
    prediction2[1] = model2[prefix2 + 'P']
    prediction2[2] = model2[prefix2 + 'S']
    model2[prefix2 + actual_suffix] += 1
    model2[prefix2 + 'R'] *= decay2
    model2[prefix2 + 'P'] *= decay2
    model2[prefix2 + 'S'] *= decay2

    prediction0 = [prediction0[i]/sum(prediction0) for i in range(3)]
    prediction1 = [prediction1[i]/sum(prediction1) for i in range(3)]
    prediction2 = [prediction2[i]/sum(prediction2) for i in range(3)]
    blend = [(prediction0[i] + prediction1[i] + prediction2[i])/3 for i in range(3)]
    
    if random.random() < blend[0] / sum(blend):
        output = "P"
    elif random.random() < blend[1] / sum(blend[1:]):
        output = "S"
    else:
        output = "R"
else:
    output = random.choice(['R','P','S'])