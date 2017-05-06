import random

RPS = ["R","P","S"]


if input == "":
    output = random.choice(RPS)
    cur = 1
    lim = 1
    last = output

elif cur < lim:
    cur += 1
    output = last

else:
    cur = 1
    lim += 1
    if last == "R":
        output = "S"
    elif last == "P":
        output = "R"
    else:
        output = "P"
    last = output