#Rock Paper Scissors AI Created By Samuel Miller 2014
import random
if input == "":
    lastMove = 0
    output = random.choice(["R","P","S"])
if input == "R":
    lastMove = "R"
elif input == "P":
    lastMove = "P"
elif input == "S":
    lastMove = "S"
def NormalStyle():
    if lastMove == "R":
        output = "S"
    elif lastMove == "P":
        output = "R"
    else:
        output = "P"
def WoahWhatTheHeak():
    if lastMove == "R":
        output = "P"
    elif lastMove == "P":
        output = "S"
    else:
        output = "R"
if lastMove == input:
    WoahWhatTheHeak()
else:
    NormalStyle()