import random
if input == "":
    opp1 = ""
    opp2 = ""
    output= "S"
    tranvar = ""
    
else:
    if random.random() < 0.5:
        output = random.choice(["R","P","S"])
    tranvar = opp2
    opp2 = opp1
    opp1 = input
    if opp1 == opp2:
        if opp1 == "R":
            output = "S"
        if opp1 == "S":
            output = "P"
        if opp1 == "P":
            output = "R"
        if opp2 == tranvar:
            if opp1 == "R":
                output = "P"
            if opp1 == "S":
                output = "R"
            if opp1 == "P":
                output = "S"

    else:
        if opp1 == "R":
            if opp2 == "S":
                output = "S"
            if opp2 == "P":
                output = "R"
        if opp1 == "S":
            if opp2 == "R":
                output = "S"
            if opp2 == "P":
                output = "P"
        if opp1 == "P":
            if opp2 == "S":
                output = "P"
            if opp2 == "R":
                output = "R"