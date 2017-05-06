import random as r
c = [["R","S"],["P","R"],["S","P"],["P","S"],["S","R"],["R","P"]]
if input:
    for i in range(len(t)):
        if input == t[i]:
            pass
        elif [input, t[i]] in c[3:]:
           s[i] += 1
        elif [input, t[i] in c[0:3]]:
           s[i] -= 1
    t[3] = r.choice(t[0:3])
    if input == "R":
        t[4] = "P"
        t[5] = "S"
        t[6] = "R"
    elif input == "P":
        t[4] = "S"
        t[5] = "R"
        t[6] = "P"
    else:
        t[4] = "R"
        t[5] = "P"
        t[6] = "S"
    b = 0
    for i in range(len(h)):
        if input == t[i]:
            h[i] += 1
        if h[i] > h[b]:
            b = i
    t[7] = t[b]
    t[8] = t[(b+1)%3]
    t[9] = t[(b-1)%3]
    b = 0
    for i in range(len(s)):
        if s[i] > s[b]:
            b = i
    output = t[b]
else:
    s = [0,0,0,0,0,0,0,0,0,0]
    h = [0,0,0]
    t = ["R","P","S","S","S","S","S","S","S","S"]
    output = "S"