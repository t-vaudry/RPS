if input == "": # initialize variables for the first round
	rockCount = paperCount = scissorsCount = 0
if rockCount > paperCount and rockCount > scissorsCount:
	rockCount = rockCount + 1
	output = "P" # paper beats rock
elif paperCount > scissorsCount:
	scissorsCount = scissorsCount + 1
	output = "S" # scissors beats paper
else:
	paperCount = paperCount + 1
	output = "R" # rock beats scissors