import random

def move(prevDir, cur):
    if prevDir == ">":
        if (cur % 10) == 9:
            cur -= 9
        else:
            cur += 1
    elif prevDir == "v":
        cur += 10
    elif prevDir == "<":
        if cur % 10 == 0:
            cur += 9
        else:
            cur -= 1
    elif prevDir == "^":
        cur -= 10
    if cur < 0:
        cur += 100
    if cur > 100:
        cur -= 100
    return cur

def funge(source):
    cur = 0
    out = ""
    options = ["R","P","S"]
    dir = [">","v","<","^"]
    prevDir = ">"
    while source[cur] != "@":
        if source[cur] == " ":
            cur = cur
        if source[cur] in dir:
            prevDir = source[cur]
        elif source[cur] == "?":
            prevDir = random.choice(dir)
        elif source[cur] in options:
            out = source[cur]
        cur = move(prevDir, cur)
    if out == "":
        out = random.choice(options)
    return out

source = ["v","@"," "," "," "," "," "," "," "," ",\
          " ","R"," "," "," "," "," "," "," "," ",\
          ">","?","P","@"," "," "," "," "," "," ",\
          " ","S"," "," "," "," "," "," "," "," ",\
          " ","@"," "," "," "," "," "," "," "," ",\
          " "," "," "," "," "," "," "," "," "," ",\
          " "," "," "," "," "," "," "," "," "," ",\
          " "," "," "," "," "," "," "," "," "," ",\
          " "," "," "," "," "," "," "," "," "," ",\
          " "," "," "," "," "," "," "," "," "," "]
output = funge(source)
print output