import random

if input == "": # initialize variables for the first round
    moves = []
    beat = "R"
    output = "P"
    round = 1
    next_r = 3
else:
    moves.append(input)

    random.shuffle(moves)
    beat = moves[0]
    if beat == "R":
        output = "P"
    elif beat == "P":
        output = "S"
    else:
        output = "R"
    
    if round == next_r:
        if output  == "R":
            output = "P"
        elif output  == "P":
            output = "S"
        else:
            output = "R"
        
    round += 1
    next_r += random.choice([2,3,4])