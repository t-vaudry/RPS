import random

game = ["R","P","S"]

if input == "":
   playedAfterPrevious = { "R": {"R":0,"P":0,"S":0}, "P": {"R":0,"P":0,"S":0}, "S": {"R":0,"P":0,"S":0} }
   output = random.choice(game)
else:
    playedAfterPrevious[previous][input] += 1
    previousPlays = playedAfterPrevious[previous]
    myOptions = []
    for x in range(0, previousPlays["R"]):
        myOptions.append("P")
    for x in range(0, previousPlays["P"]):
        myOptions.append("S")
    for x in range(0, previousPlays["S"]):
        myOptions.append("R")
    if len(myOptions) > 0:
        output = random.choice(myOptions)
    else:
        output = random.choice(game)
        
previous = output