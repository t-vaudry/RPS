#Created by David Catt (2013)
#Finds the highest order matching context and copies output
import random
if input == "":
    maxord = 11
    winmap = {"R":"P","P":"S","S":"R"}
    valmap = {"R":1,"P":2,"S":3}
    maxctx = 4**maxord
    otbl = ["-"] * maxctx
    octx = 0
    ttbl = ["-"] * maxctx
    tctx = 0
    last = "R"
else:
    tmp = maxctx
    for i in range(0, maxord):
        otbl[octx % tmp] = input
        ttbl[tctx % tmp] = input
        tmp /= 4
    octx = ((4 * octx) + valmap[last]) % maxctx
    tctx = ((4 * tctx) + valmap[input]) % maxctx
tmp = maxctx
output = ""
oout = ""
oord = 0
tout = ""
tord = 0
for i in range(0, maxord):
    if oout == "":
        if otbl[octx % tmp] != "-":
            oout = winmap[otbl[octx % tmp]]
            oord = maxord - i
    if tout == "":
        if ttbl[tctx % tmp] != "-":
            tout = winmap[ttbl[tctx % tmp]]
            tord = maxord - i
    tmp /= 4

if tout == "" and oout == "":
    output = random.choice(["R","P","S"])
elif tout == "":
    output = oout
elif oout == "":
    output = tout
else:
    oprb = 3**(oord+1)
    tprb = 3**tord
    if random.randint(1, oprb + tprb) < oprb:
        output = oout
    else:
        output = tout
last = output