if input == "": # initialize variables for the first round
	rockCount = paperCount = scissorsCount = 0
elif input == "R":
	rockCount += 1
elif input == "P":
	paperCount += 1
elif input == "S":
	scissorsCount += 1
if rockCount > paperCount and rockCount > scissorsCount:
	output = "R" # paper beats rock
elif paperCount > scissorsCount:
	output = "P" # scissors beats paper
else:
	output = "S" # rock beats scissors