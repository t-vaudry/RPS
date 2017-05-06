import random

encode = {'R': 1, 'P': 2, 'S': 3}
decode = {1: 'R', 2: 'P', 3: 'S'}

if not input:
  turn = 0
  oppStack = []
else:
  turn += 1
  oppStack.append(encode[input])

if turn < 2:
  output = random.choice(('R', 'P', 'S'))
else:
  output = decode.get(sum(oppStack[-20::]) % 4, random.choice(('R', 'P', 'S')))