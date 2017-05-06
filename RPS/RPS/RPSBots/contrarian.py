import itertools
import random

STRINGS = ['R', 'P', 'S']
HISTORY = {}
for one in [0, 1, 2]:
    for two in [0, 1, 2]:
        HISTORY[(one, two)] = {0: 0, 1:0, 2:0}
LAST3 = ''

if input == '':
    output_num = random.choice([0,1,2])
    LAST3 += input
elif len(LAST3) < 3:
    LAST3 += input
    output_num = random.choice([0, 1, 2])
else:
    context = LAST3[:-1]
    history[context][LAST3[-1]] += 1
    LAST3 = LAST3[1:] + input
    output_num = min(history[context], key=lambda k: history[context][k])
    
output = STRINGS[output_num]