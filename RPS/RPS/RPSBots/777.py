import random
if input == "":
    count = [7,7,7]
elif input == "R":
    count[0] += 1
elif input == "P":
    count[1] += 1
elif input == "S":
    count[2] += 1
if random.randint(1,sum(count)) <= count[0]:
    output = "P"
elif random.randint(1,sum(count[1:])) <= count[1]:
    output = "S"
else:
    output = "R"