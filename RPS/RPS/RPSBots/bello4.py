import random
if input == "": # initialize variables for the first round
	rockCount = paperCount = scissorsCount = count = 0
elif input == "R":
	rockCount += 1
elif input == "P":
	paperCount += 1
elif input == "S":
	scissorsCount += 1
if count < 10:
        output = random.choice(["R","P","S"])
elif count % 10 == 0:
      output = random.choice(["R","P","S"])        
elif rockCount > paperCount and rockCount > scissorsCount:
	output = "P" # paper beats rock
elif paperCount > scissorsCount:
	output = "S" # scissors beats paper
else:
	output = "R" # rock beats scissors