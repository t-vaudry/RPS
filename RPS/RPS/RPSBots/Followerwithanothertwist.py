import random
if input == '':
    output = 'R'
elif random.choice(['k', 'k', 'k', 'k', 'k', 'k', 'o']) == 'k':
    output = input
else:
    output = {'R':'S', 'P':'R', 'S':'P'}[input]