import random

if input == "":
    weights = {
        "R" : 0.0,
        "P" : 0.0,
        "S" : 0.0
    }
    output = "R"

if input == "R":
    weights["R"] += 1
    weight = (weights["R"])/(weights["R"] + weights["P"])
    ran = random.random()
    if weight > ran:
        output = "P"
    else:
        output = "R"
    
elif input == "P":
    weights["P"] += 1
    weight = (weights["P"])/(weights["P"] + weights["S"])
    ran = random.random()
    if weight > ran:
        output = "S"
    else:
        output = "P"
elif input == "S":
    weights["S"] += 1
    weight = (weights["S"])/(weights["S"] + weights["R"])
    ran = random.random()
    if weight > ran:
        output = "R"
    else:
        output = "S"