# drum v2

import random

if input == '':
    history = ["R", "P", "S"]
else:
    history.append(input)

what_beats = {"R": "P", "P": "S", "S": "R"}

x = random.choice(history[-30:])
output = what_beats[x]