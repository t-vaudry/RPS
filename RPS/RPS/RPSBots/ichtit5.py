import random


if input == "":
    opponentPlays = []
    myPlays = []
    o = random.choice(["R", "P", "S"])

else:
    opponentPlays.append(input)
    if (len(opponentPlays) < 6):
        o = random.choice(["R", "P", "S"])
    else:
        rc = 0
        pc = 0
        sc = 0
        for i in range(3, 4):
            patterns = []
            for j in range(0, len(opponentPlays)-i-1):
                patterns.append(opponentPlays[j:j+i+1])
                
                
            curPattern = opponentPlays[len(opponentPlays)-i:len(opponentPlays)]
            rc += patterns.count(curPattern+["R"])
            pc += patterns.count(curPattern+["P"])
            sc += patterns.count(curPattern+["S"])
 
        if (rc > pc and rc > sc):
            o = "P"
        elif (pc > sc):
            o = "S"
        else:
            o = "R"
            

        
myPlays.append(o)
output = o