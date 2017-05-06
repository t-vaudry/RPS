import random
if not input:
    up = 0
    cycle = 0
up = up + 1
if up>7:
    cycle = cycle + 1
    up = 0
if cycle%2:
    output = random.choice(['R','P','S'])
else:
    output = 'RPS'[(cycle/2) % 3]