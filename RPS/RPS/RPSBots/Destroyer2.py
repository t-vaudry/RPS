import random


if input == '':
        r = 0
        s = 0
        p = 0
        output = 'R'
else:
        if input == 'R':
                r += 1
        elif input == 'S':
                s += 1
        elif input == 'P':
                p += 1
        output = random.choice(['S'] * p + ['P'] * r + ['R'] * s)