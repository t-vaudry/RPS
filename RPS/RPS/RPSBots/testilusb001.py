if input == "": # initialize variables for the first round
	rockCount = paperCount = scissorsCount = 1
        minus = 0.33333333333333
        summ = 3
elif input == "R":
	rockCount += 1
elif input == "P":
	paperCount += 1
elif input == "S":
	scissorsCount += 1
if rockCount/summ > paperCount/summ and rockCount/summ > scissorsCount/summ:
	output = "P" # paper beats rock
elif paperCount/summ > scissorsCount/summ:
	output = "S" # scissors beats paper
else:
	output = "R" # rock beats scissors
rockCount -= minus
paperCount -= minus
scissorsCount -= minus
summ = rockCount + paperCount+scissorsCount