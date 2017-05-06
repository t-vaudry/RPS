import random

input = ""
if input=="":
    context = [""] * 4

print input

htable = dict()

ctx = "_".join(context)
print ctx

simple = dict()
simple["R"]=1
simple["S"]=1
simple["P"]=1
total = 3

beta = random.random()
gamma = random.random()

if ctx in htable and beta<0.8:
    r = htable[ctx]["R"]
    p = htable[ctx]["P"]
    s = htable[ctx]["S"]
    pr = float(r)/(r+p+s)
    pp = float(p)/(r+p+s)
    ps = float(s)/(r+p+s)
    pos = ['R'] * htable[ctx]["R"] + ['P'] * htable[ctx]['P'] + ['S'] * htable[ctx]['S']
    output = random.choice(pos)
else:
    if input != "":
        htable[ctx]=dict()
        htable[ctx]["R"]=0
        htable[ctx]["P"]=0
        htable[ctx]["S"]=0
        htable[ctx][input]+=1
    pos = ['R'] * simple["R"] + ['P'] * simple['P'] + ['S'] * simple['S']
    output = random.choice(pos)

context.pop(0)
context.append(input)
if input!="":
    simple[input]+=1
    total+=1

print output
print "--------------"