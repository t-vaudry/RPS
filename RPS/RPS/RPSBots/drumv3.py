# drum v3

import random

if input == '':
    history = ["R", "P", "S"]
else:
    history.append(input)

what_beats = {"R": "P", "P": "S", "S": "R"}

base = ['R', 'P', 'S']
last_two = history[-2:]
for (a, b, next) in zip(history, history[1:], history[2:]):
    if [a, b] == last_two:
        base.append(next)

x = random.choice(base)
output = what_beats[x]