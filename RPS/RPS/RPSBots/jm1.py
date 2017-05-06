import random
if input == "": 
    rockCount = paperCount = scissorsCount = 0
    currentduration = 0
    currentoutput = ""
    
if currentduration <= 0:
    currentduration = random.randrange(10)
    currentoutput = random.choice(["R","P","S"])
    currentduration = currentduration = 1

output = currentoutput