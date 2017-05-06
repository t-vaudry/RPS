import random

if input == "":
    rps = list('RPS')
    points = [0] * 3
    output = random.choice(rps)
    total = 0
else:
    oidx = rps.index(input)
    points[(oidx+1)%3] += 2
    points[oidx] += 1
    total += 3
    r = random.randint(0,total-1)
    output = ""
    if r < points[0]:
        output = 'R'
    elif r < points[0] + points[1]:
        output = 'P'
    elif r < points[0] + points[1] + points[2]:
        output = 'S'