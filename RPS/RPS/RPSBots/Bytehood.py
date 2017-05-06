if input == "": 
	rockCount = paperCount = scissorsCount = 0
elif input == "R":
	rockCount += 1
elif input == "P":
	paperCount += 1
elif input == "S":
	scissorsCount += 1
if rockCount > paperCount and rockCount > scissorsCount:
	output = "P" 
elif paperCount > scissorsCount:
	output = "S"
else:
	output = "R"