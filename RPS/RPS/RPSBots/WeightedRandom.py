#Created by David Catt on December 12, 2014
import random
if input == "":
    winner = {0:"P",1:"S",2:"R"}
    value = {"R":0,"P":1,"S":2}
    order = 3
    decay = 0.93
    mask = 3**(order+1)
    prob = [1.0] * mask
    ctx = 0
else:
    val = value[input]
    prob[ctx    ] *= decay
    prob[ctx+  1] *= decay
    prob[ctx+  2] *= decay
    prob[ctx+val] += 1.0
    ctx = ((ctx + val) * 3) % mask
p0 = prob[ctx]
p1 = prob[ctx+1]
p2 = prob[ctx+2]
rn = random.random() * (p0 + p1 + p2)
tv = 0
if rn <= p0:
    tv = 0
elif rn <= p1:
    tv = 1
else:
    tv = 2
output = winner[tv]