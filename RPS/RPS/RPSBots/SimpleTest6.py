import random
from math import ceil
if input == "":
    a = 10
    b = 10
    c = 10
    wins = {'R':'P', 'P':'S', 'S':'R'}
elif wins[input] == last:
    if last == 'R':
        a = int(ceil(a * random.random() * random.randrange(1,3)))
    elif last == 'P':
        b = int(ceil(b * random.random() * random.randrange(1,3)))
    else:
        c = int(ceil(c * random.random() * random.randrange(1,3)))
    
l = ['R']*random.randrange(1,a+1) + ['P']*random.randrange(1,b+1) + ['S']*random.randrange(1,c+1)
output = random.choice(l)
last = output