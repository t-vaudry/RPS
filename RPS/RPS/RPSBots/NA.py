if input=="": # initialize variables for the first round
	rockCount = paperCount = scissorsCount = 0
if input == "R":
	output = "P" # paper beats rock
elif input == "P":
	output = "S" # scissors beats paper
else:
	output = "R" # rock beats scissors