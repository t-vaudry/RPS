import random

if input == "": # initialize variables for the first round
    output = "P"
    round = 1
    next_r = 3
else:
    if round == next_r:
        output = "R"
        next_r += random.choice([2,3])
    else:
        output = random.choice(["S","P"])
        
    round += 1