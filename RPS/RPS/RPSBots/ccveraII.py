if input=="": # initialize variables for the first round
	rockCount = paperCount = scissorsCount = totalCount = 0
elif input == "R":
	rockCount += 1
elif input == "P":
	paperCount += 1
elif input == "S":
	scissorsCount += 1

totalCount += 1


import random
output = random.choice(["R","P",random.choice(["S","R"])])