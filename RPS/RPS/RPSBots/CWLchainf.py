import random

if input == "": # initialize variables for the first round
    moves = []
    beat = "R"
    output = "P"
    round = 1
    next_r = 3
    chain = 0
    to_chain = "S"
    in_chain = False
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
    
    if in_chain == True:
        output = to_chain
        chain += 1
        if chain == 3:
            in_chain = False
            
    if round % 150 == 0:
        in_chain = True
        to_chain = output
        chain = 0