import random

encode = {'R': 0, 'P': 1, 'S': 2}
decode = {0: 'R', 1: 'P', 2: 'S'}

if not input:
  turn = 0
  oppStack = []
else:
  turn += 1
  oppStack.append(encode[input])

if turn < 2:
  output = random.choice(('R', 'P', 'S'))
else:
  output = decode[sum(oppStack[-20::]) % 3]