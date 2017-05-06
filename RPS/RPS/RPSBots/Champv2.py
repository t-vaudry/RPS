import random

if not input:
    counter = dict()
    counter['R'] = counter['P'] = counter['S'] = 0
else:
    counter[input] += 1

pool = [letter for letter in 'RPS' if counter[letter] == max(counter.values())]
crystal_ball = pool[random.randrange(len(pool))]
output = 'RPS'[('RPS'.index(crystal_ball) + 1) % 3]