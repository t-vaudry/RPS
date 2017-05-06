import random
if input == "":
    l = ['R']*random.randrange(1,100) + ['P']*random.randrange(1,100) + ['S']*random.randrange(1,100)
output = l.pop(0)
l.append(output)