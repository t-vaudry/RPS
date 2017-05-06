import zlib
import random

if input == "":
    rockCount = paperCount = scissorsCount = 0
    interleaved = []
    opponent = []
elif input == "R":
    rockCount += 1
elif input == "P":
    paperCount += 1
elif input == "S":
    scissorsCount += 1

def new_size(history, new_move):
    s = "".join(history) + new_move
    c = zlib.compress(s, 9)
    return len(c)
    
    
if input == "":
    output = random.choice(["R", "P", "S"])
else:
    sizes = [
        new_size(interleaved, "R"),
        new_size(interleaved, "P"),
        new_size(interleaved, "S"),
        new_size(opponent, "R"),
        new_size(opponent, "P"),
        new_size(opponent, "S")
    ]
    beating_moves = [
        "P", 
        "S", 
        "R",
        "P", 
        "S", 
        "R"
    ]
    output = beating_moves[sizes.index(min(sizes))]
    
interleaved.append(input)
interleaved.append(output)
opponent.append(input)