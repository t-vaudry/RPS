# Decaying Bot
# Most recent moves made by opponent are weighted more heavily
#

import math
import random

if not input: # Initilize ratings
    rRating = sRating = pRating = 0
else :
    # Decay old ratings by 10% each iteration
    rRating *= 0.9
    pRating *= 0.9
    sRating *= 0.9    

if input == "R": # Increase rating of RPS that will beat current input
    pRating += 0.25
    sRating -= 0.25
elif input == "P":
    sRating += 0.25
    rRating -= 0.25
elif input == "S":
    rRating += 0.25
    pRating -= 0.25

expRock = math.exp(rRating)
expScissors = math.exp(sRating)
expPaper = math.exp(pRating)

Rating = random.random()* (expRock + expScissors + expPaper)
if Rating < expRock:
    output = "R"
elif Rating < (expRock + expPaper):
    output = "P"
else:
    output = "S"