import random

if input == "":
    others = {"R": 0, "P": 0, "S": 0}
    beat = {"R": "P", "P": "S", "S": "R"}
    output = random.choice(beat.keys())
    history = [output]
else:
    history[-1] = (input, history[-1])
    others[beat[input]] += 1
    moves = dict((k,v*2.5) for k,v in others.items())
    for i in xrange(max(len(history)-100,0),len(history)-1):
        for j in xrange(min(i+1,8)):
            
            if history[i-j] == history[-j-2]:
                moves[beat[history[i+1][0]]] += j
            else:
                break
    output = random.random() * sum(moves.values())
    if output < moves["R"]:
        output = "R"
    elif output < moves["R"] + moves["P"]:
        output = "P"
    else:
        output = "S"
    history.append(output)