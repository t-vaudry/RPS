import random

if not input:
    his = ["R","S","P"]
else:
    his.append(input)

random.shuffle(his)
output = his[0]