import random
if input == '':
   s = 1
   n = 1
s -= 1
n += 1
if s >= 0:
    choice = random.choice('RPS')
    s = random.randint(1, n)
output = choice