import random

options = list('RPS') * random.randint(3, 13)
random.shuffle(options)
output = random.choice(options)