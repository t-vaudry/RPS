import random

if input == '':
    history = ["R", "P", "S"]
else:
    history.append(input)

what_beats = {"R": "P", "P": "S", "S": "R"}

x = random.choice(history)
output = what_beats[x]