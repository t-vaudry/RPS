import random

if input == "":
    gamesplayed = 0

gamesplayed = gamesplayed + 1
if gamesplayed < 400:
    output = "R"
else:
    output = "S"
    
random.seed(0)