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
        #for i in range(3, len(opponentPlays)/2):
        for i in range(3, 4):
            patterns = []
            for j in range(0, len(opponentPlays)-i-1):
                patterns.append(opponentPlays[j:j+i+1])
                
                
            curPattern = opponentPlays[len(opponentPlays)-i:len(opponentPlays)]
            print curPattern
            curPattern.append("R")
            
            rc += patterns.count(curPattern)
            curPattern.pop()
            
            curPattern.append("P")
            pc += patterns.count(curPattern)
            curPattern.pop()
            
            curPattern.append("S")
            sc += patterns.count(curPattern)
 
        if (rc > pc and rc > sc):
            o = "P"
        elif (pc > sc):
            o = "S"
        else:
            o = "R"
            

        
myPlays.append(o)
output = o