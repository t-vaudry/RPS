#Weights Recent Hands
#Weights set to win 70% against FirstTest51213

import random

if input == "":
    rockCount = paperCount = scissorsCount = 10 #to avoid divide by 0
elif input == "R":
	rockCount *= 1.5
	paperCount *= .8
	scissorsCount *= .8
elif input == "P":
	paperCount *= 1.5
	scissorsCount *= .8
	rockCount *= .8
elif input == "S":
	scissorsCount *= 1.5
	rockCount *= .8
	paperCount *= .8

pRock = rockCount
pPaper = paperCount
pScissors = scissorsCount

total = float(pRock + pPaper + pScissors)

probRock = pRock/total
probPaper = pPaper/total
probScissors = pScissors/total

prob = random.random()

if prob < probRock:
	output = "P" # paper beats rock
elif prob < (probPaper + probRock):
	output = "S" # scissors beats paper
else:
	output = "R" # rock beats scissors