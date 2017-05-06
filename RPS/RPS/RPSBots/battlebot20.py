import random

if input:
    his.append(input)
else:
    his = ["R","P","S"]

beat = {"R":"P","P":"S","S":"R"}

random.shuffle(his)

output = beat[his[0]]