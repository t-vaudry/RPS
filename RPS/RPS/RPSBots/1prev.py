import random

if input=="":
    output = random.choice(['R', 'P', 'S'])
else:
    if input == 'R':
        output = 'P'
    elif input == 'P':
        output = 'S'
    else:
        output = 'R'