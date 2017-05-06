if input == "": # initialize variables for the first round
        lastMove = ""
elif input == "R":
        lastMove = "R"
elif input == "P":
        lastMove = "P"
elif input == "S":
        lastMove = "S"

if lastMove == "R":
	output = "P" # paper beats rock
elif lastMove == "P":
	output = "S" # scissors beats paper
else:
	output = "R" # rock beats scissors