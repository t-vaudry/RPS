import random
if not input:
    history = ""
    output = "R"
    turnaround = 500
    match = 1
    count = 0
    beat={'R':'P','P':'S','S':'R'}
else:
    match += 1
    history += input
            
    if match == turnaround:
        history = history[::-1]
    
    if match > turnaround:
        output = beat[history[count:count+1:]]
        count += 1
    else:
        output = random.choice(["R","P","S"])