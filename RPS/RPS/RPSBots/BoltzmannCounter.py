import math
import random

if not 'rockRating' in dir(): # initialize variables for the first round
    rockRating = scissorsRating = paperRating = 0
rockRating *= 0.95
scissorsRating *= 0.95
paperRating *= 0.95
if input == "R":
    paperRating += 0.1
    scissorsRating -= 0.1
elif input == "P":
    scissorsRating += 0.1
    rockRating -= 0.1
elif input == "S":
    rockRating += 0.1
    paperRating -= 0.1

randNum = random.random()*(math.exp(rockRating)+math.exp(scissorsRating)+math.exp(paperRating))

if randNum < math.exp(rockRating):
    output = "R"
elif randNum < math.exp(rockRating) + math.exp(paperRating):
    output = "P"
else:
    output = "S"
print output