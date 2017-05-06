import random

##using x**5 instead of x**3
##see FirstTest51213

if input == "":
    rockCount = paperCount = scissorsCount = 1 #to avoid divide by 0
elif input == "R":
	rockCount += 1
elif input == "P":
	paperCount += 1
elif input == "S":
	scissorsCount += 1

pRock = rockCount**5
pPaper = paperCount**5
pScissors = scissorsCount**5

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