from random import choice

if input == '':
    freq = dict.fromkeys('RPS', 1)
else:
    freq[input] += 1

output = choice(''.join(k*v for k, v in freq.items()))
output = dict(R='P', P='S', S='R')[output]