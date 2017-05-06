import random

input = ""
if input=="":
    context = [""] * 4
    my_context = [""] * 4


htable = dict()
htable2 = dict()

ctx = "_".join(context)
my_ctx = "_".join(my_context)

simple = dict()
simple["R"]=1
simple["S"]=1
simple["P"]=1
total = 3

beta = random.random()
gamma = random.random()


# Study if my context is in table and what the bot played to my context
if my_ctx in htable2:
    r = htable2[my_ctx]["R"]
    p = htable2[my_ctx]["P"]
    s = htable2[my_ctx]["S"]
    pr2 = float(r)/(r+p+s)
    pp2 = float(p)/(r+p+s)
    ps2 = float(s)/(r+p+s)
    proba = max([pr2,pp2,ps2])
    pos = ['R'] * htable2[my_ctx]["R"] + ['P'] * htable2[my_ctx]['P'] + ['S'] * htable2[my_ctx]['S']
    output = random.choice(pos)
    if output == "R":
        output = "P"
    elif output =="P":
        output = "S"
    else:
        output = "R"
else:
    if input != "":
        htable2[my_ctx]["R"]=0
        htable2[my_ctx]["P"]=0
        htable2[my_ctx]["S"]=0
        htable2[my_ctx][input]+=1

if ctx in htable and beta<0.9:
    r = htable[ctx]["R"]
    p = htable[ctx]["P"]
    s = htable[ctx]["S"]
    pr = float(r)/(r+p+s)
    pp = float(p)/(r+p+s)
    ps = float(s)/(r+p+s)
    pos = ['R'] * htable[ctx]["R"] + ['P'] * htable[ctx]['P'] + ['S'] * htable[ctx]['S']
    if proba<max([pr,pp,ps]):
        output = random.choice(pos)
        if output == "R":
            output = "P"
        elif output =="P":
            output = "S"
        else:
            output = "R"
else:
    if input != "":
        htable[ctx]=dict()
        htable[ctx]["R"]=0
        htable[ctx]["P"]=0
        htable[ctx]["S"]=0
        htable[ctx][input]+=1
    if gamma<0.5:
        pos = ['R'] * simple["R"] + ['P'] * simple['P'] + ['S'] * simple['S']
    else:
        pos = ["R","S","P"]
    output = random.choice(pos)
    if output == "R":
        output = "P"
    elif output =="P":
        output = "S"
    else:
        output = "R"

context.pop(0)
context.append(input)
my_context.pop(0)
my_context.append(output)

if input!="":
    simple[input]+=1
    total+=1