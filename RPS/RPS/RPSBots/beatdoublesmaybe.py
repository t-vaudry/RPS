import random
doubles = {"R": "S", "P": "R", "S": "P"}

if input == "":
    output = "S"
    opponents_moves = []
    my_moves = []
    count = 0
else:
    opponents_moves.append(input)
    my_moves.append(output)
    if count < 2:
        output = random.choice(["R","P","S"])
    else:
        if opponents_moves[count] == opponents_moves[count-1]:
            output = doubles[opponents_moves[count]]
        else:
            output = random.choice(["R","P","S"])