import random
rCount = pCount = sCount = 0
if input == "":
    # init counter variables if input is blank
    rCount = pCount = sCount = 0
    # output is then random
    output = random.choice(["R","P","S"])
elif input == "R":
    rCount += 1
elif input == "P":
    pCount += 1
elif input == "S":
    sCount += 1

if rCount > pCount and rCount > sCount:
    output = "P"
elif pCount > sCount and pCount > rCount:
    output = "S"
elif sCount > pCount and sCount > rCount:
    output = "R"