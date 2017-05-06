import random
if input == "":
    l = ['R']*random.randrange(1,10) + ['P']*random.randrange(1,10) + ['S']*random.randrange(1,10)
output = l.pop(0)
l.append(output)