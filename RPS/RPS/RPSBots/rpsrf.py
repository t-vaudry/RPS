import random

w = {'RR':0, 'RP':-1, 'RS':1,
     'PP':0, 'PS':-1, 'PR':1,
     'SS':0, 'SR':-1, 'SP':1}

b = {'R':'P', 'S':'R', 'P':'S'}

if input == "":
    me, you = "", ""


output = random.choice(['R','P','S'])
you += input


if input == "":
    count = 0
    score = 0
else:
    count += 1
    score += w[me[-1] + input]


if count > 50:

    s = you[-2:]

    best = 0
    a = ""

    for third in "RPS":
        ss = s + third
        c = you.count(ss)
        if c > best:
            best = c
            a = third

    if best >= count / 10:
        output = b[a]


me += output