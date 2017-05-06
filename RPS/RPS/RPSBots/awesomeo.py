import random
if input == "":
    BEATS = {
        "R":{
            "R":0,
            "P":-1,
            "S":1,
        },
        "P":{
            "R":1,
            "P":0,
            "S":-1,
        },
        "S":{
            "R":-1,
            "P":1,
            "S":0,
        },
    }
    ONE_UP = { "S":"R", "R":"P", "P":"S" }
    history_you, history_me = "",""
    plusminus,throws,wins = 0,0,0
    output = random.choice(["R","P","S"])
    
    trials = 0
    last_score = .1
    cycle_history = ""
    arockCount = apaperCount = ascissorsCount = 0
    cycles = 0
else:
    history_you += input
    throws += 1
    
    #calculate plusminus
    plusminus += BEATS[history_me[-1]][history_you[-1]]
    if BEATS[history_me[-1]][history_you[-1]] > 0: wins += 1
    
    # initial strategy

    if history_me[-1] == "R":
        arockCount += 1
    elif history_me[-1] == "P":
        apaperCount += 1
    elif history_me[-1] == "S":
        ascissorsCount += 1
    if arockCount > apaperCount and arockCount > ascissorsCount:
        output = "P" # paper beats rock
    elif apaperCount > ascissorsCount:
        output = "S" # scissors beats paper
    else:
        output = "R" # rock beats scissors
    
    score = 0
    a = 1

    if random.randint(0,10) < trials:
        for x in range(min(10, throws)):
            try:
                score += a * BEATS[history_me[throws-x-1]][history_you[throws-x-1]]
                a *= .9
            except IndexError:
                pass
        if score <= last_score:
            cycles = (cycles + 1) % 3
        last_score = score
        trials = 0
    trials += 1
    for i in range(cycles):
        output = ONE_UP[output]
cycle_history += str(cycles)
history_me += output