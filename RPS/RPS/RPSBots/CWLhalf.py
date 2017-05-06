import random

if input == "": # initialize variables for the first round
    moves = []
    beat = "R"
    output = "S"
    round = 1
    next_r = 3
else:    
    moves.append(input)
    batch = moves[len(moves)/2:]
    random.shuffle(batch)
    beat = batch[0]
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
    next_r += random.choice([4,5,6])