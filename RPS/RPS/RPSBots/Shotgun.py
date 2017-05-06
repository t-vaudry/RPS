import random as r

c = [["R","S"],["P","R"],["S","P"],["P","S"],["S","R"],["R","P"]]
if input:
    for i in range(len(t)):
        if [input, t[i]] in c[0:3]:
            s[i] += 1
        elif [input, t[i] in c[3:6]]:
            s[i] -= 1
    t[3] = r.choice(t[0:3])
    if input == "R":
        t[4] = "P"
        t[5] = "S"
    elif input == "P":
        t[4] = "S"
        t[5] = "R"
    else:
        t[4] = "R"
        t[5] = "P"
    b = 0
    for i in range(len(s)):
        if s[i] > s[b]:
            b = i
    output = t[b]
else:
    t = ["R","P","S","S","S","S"]
    s = [0,0,0,0,0,0]
    output = "S"