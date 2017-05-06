import random

if input == "": # initialize variables for the first round
	rockCount = paperCount = scissorsCount = 0
elif input == "R":
	rockCount += 1
elif input == "P":
	paperCount += 1
elif input == "S":
	scissorsCount += 1


n = paperCount + scissorsCount + rockCount
rockSmooth = (30.0 + rockCount) / (90.0 + n)
paperSmooth = (30.0 + paperCount) / (90.0 + n)
scissorsSmooth = (30.0 + scissorsCount) / (90.0 + n)

rockL = scissorsSmooth
paperL = rockSmooth
scissorsL = paperSmooth

if( n <= 199 ):
    rockL *= 0.36
    paperL *= 0.32
    scissorsL *= 0.32
elif( n <= 799):
    rockL *= 0.30
    paperL *= 0.32
    scissorsL *= 0.38
else:
    rockL *= 0.34
    paperL *= 0.40
    scissorsL *= 0.26


divL = rockL + paperL + scissorsL
rockP = rockL / divL
paperP = paperL / divL
scissorsP = scissorsL / divL

k = random.random()

if( k < rockP ):
    output = "R"
elif( k < rockP + paperP ):
    output = "P"
else:
    output = "S"