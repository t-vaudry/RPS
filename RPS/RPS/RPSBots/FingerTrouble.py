from random import choice
if input == '':
    R,P,S = 'RPS'
    beats = dict(R=P, P=S, S=R)
better = beats.get(input, S)
output = choice('RPS' + better)