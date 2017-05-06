import random as e
if input:
    if g == input:
        s[0] += 1
else:
    s = [0,0]
    c = [("R","P"),("P","S"),("S","R")]
g =  e.choice(["R","P","S"])
if e.randint(0,s[1]) < s[0]:
    for i in c:
        if g == i[0]:
            output = i[1]
else:
    output = g
s[1] += 1