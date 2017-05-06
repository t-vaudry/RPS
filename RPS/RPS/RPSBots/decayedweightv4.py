import random
if input == "":
    count = [13.0, 13.0, 13.0]
else:
    for i in range(len(count)):
        count[i] *= 0.91
    if input == "R":
        count[0] += 1
    elif input == "P":
        count[1] += 1
    elif input == "S":
        count[2] += 1
if random.random() < count[0] / sum(count):
    output = "P"
elif random.random() < count[1] / sum(count[1:]):
    output = "S"
else:
    output = "R"