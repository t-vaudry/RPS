#Created by David Catt (2013)
#A losing version of my CopyFind2 program
#Finds the highest order matching context and copies output
import random
if input == "":
    maxord = 10
    winmap = {"R":"S","P":"R","S":"P"}
    valmap = {"R":1,"P":2,"S":3}
    maxctx = 4**maxord
    table = ["-"] * maxctx
    ctx = 0
    last = "R"
else:
    tmp = maxctx
    for i in range(0, maxord):
        table[ctx % tmp] = input
        tmp /= 4
    ctx = ((4 * ctx) + valmap[last]) % maxctx
tmp = maxctx
output = ""
for i in range(0, maxord):
    if output == "":
        if table[ctx % tmp] != "-":
            output = winmap[table[ctx % tmp]]
    tmp /= 4
if output == "":
    output = random.choice(["R","P","S"])
last = output