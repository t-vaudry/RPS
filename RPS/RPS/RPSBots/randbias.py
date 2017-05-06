import random
if input == "": # initialize variables for the first round
	rockCount = paperCount = scissorsCount = 0
elif input == "R":
	rockCount += 1
elif input == "P":
	paperCount += 1
elif input == "S":
	scissorsCount += 1
r = random.randint(0,rockCount+paperCount+scissorsCount)
if r <= rockCount:
	output = "P"
elif r<= rockCount+paperCount:
	output = "S"
else:
	output = "R"