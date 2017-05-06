import random

rps = ['R','P','S']

if not input:
    output = random.choice(rps)
else:
    output = rps[(rps.index( input ) - rps.index( output )) % 3]