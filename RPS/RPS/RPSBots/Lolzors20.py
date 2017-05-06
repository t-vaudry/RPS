import random

MAX = 40

if input == "":
    window = []
    output = random.choice(['P','R','S'])
else:
    window.append(input)
    if len(window) > MAX:
        window = window[1:MAX]

    p = 0
    r = 0
    s = 0
    for i in window:
        i = i.strip()
        if i == 'P':
            p += 1
        elif i == 'R':
            r += 1
        elif i == 'S':
            s += 1

    if p >= r and p >= s:
        output = 'S'
    elif r >= p and r >= s:
        output = 'P'
    elif s >= p and s >= r:
        output = 'R'
    else:
        output = 'R'