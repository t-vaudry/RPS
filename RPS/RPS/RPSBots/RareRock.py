import random

if input == "": # initialize variables for the first round
    moves = []
    beat = "R"
    output = "R"
    round = 1
    next_r = 3
else:
    if round == next_r:
        output = "R"
        next_r += random.choice([3,4,5,6,7,8])
    else:
        output = random.choice(["S","P"])
        
    round += 1