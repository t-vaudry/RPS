import random

if input == '':
    throws = ''
else:
    throws += input

len_throws = len(throws)
x = throws.replace('R', '')
num_r = len_throws - len(x)
x = throws.replace('P', '')
num_s = len(x)
num_p = len_throws - num_r - num_s

options = [(num_r, random.random(), 'R'), (num_p, random.random(), 'P'), (num_s, random.random(), 'S')]
options.sort()

output = options[-1][2]
throws += output