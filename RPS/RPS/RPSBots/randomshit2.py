if input=="": # initialize variables for the first round
	rockCount = 150
        paperCount = 100
        scissorsCount = 50
if input == "R":
	rockCount += 2
elif input == "P":
	paperCount += 3
elif input == "S":
	scissorsCount += 1
if rockCount > paperCount and rockCount > scissorsCount:
	output = "P" # paper beats rock
elif paperCount > scissorsCount:
	output = "S" # scissors beats paper
else:
	output = "R" # rock beats scissors