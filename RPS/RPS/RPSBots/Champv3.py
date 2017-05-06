import random

if not input:
    output = 'RPS'[random.randrange(3)]
else:
    output = 'RPS'[('RPS'.index(input) + 1) % 3]