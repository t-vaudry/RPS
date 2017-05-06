import random

if input == "":
    rockCount = paperCount = scissorsCount = 1 #to avoid divide by 0
elif input == "R":
	rockCount += 1
elif input == "P":
	paperCount += 1
elif input == "S":
	scissorsCount += 1

pRock = rockCount**3
pPaper = paperCount**3
pScissors = scissorsCount**3

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