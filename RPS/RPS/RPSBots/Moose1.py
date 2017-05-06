#Rock Paper Scissors AI Created By Samuel Miller 2014
import random
if input == "":
    lastMove = 0
    output = random.choice(["R","P","S"])
elif input == "R":
    lastMove = "R"
elif input == "P":
    lstMove = "P"
elif input == "S":
    lastMove = "S"
if lastMove == "R":
    output = "S"
elif lastMove == "P":
    output = "R"
else:
    output = "P"