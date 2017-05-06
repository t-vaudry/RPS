import random

if input == "":
	rockCount = paperCount = scissorsCount = round = 0
elif input == "R":
	rockCount += 1
elif input == "P":
	paperCount += 1
elif input == "S":
	scissorsCount += 1
if round < 500:
        output = random.choice(["R","P","S"])
elif rockCount > paperCount and rockCount > scissorsCount:
	output = "P"
elif paperCount > scissorsCount:
	output = "S"
else:
	output = "R"

round += 1