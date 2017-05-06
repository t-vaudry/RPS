import random
if input == '':
    output = 'R'
elif random.choice(['k', 'k', 'k', 'k', 'k', 'k', 'o']) == 'k':
    output = input
else:
    output = random.choice(["R","P","S"])