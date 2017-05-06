import random
if input == "":
    l = {'R':'P', 'P':'S', 'S':'R'}
    m = ['R', 'P', 'S']
else:
    if l[last] == input:
        m.append(input)
output = random.choice(m)
        
last = output