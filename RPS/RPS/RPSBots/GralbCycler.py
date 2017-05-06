if input == "":
	rockCount = paperCount = scissorsCount = 0
elif input == "R":
	rockCount += 1
elif input == "P":
	paperCount += 1
elif input == "S":
	scissorsCount += 1

totalCount = rockCount + paperCount + scissorsCount
if(totalCount % 3 == 0):
    output = "R"
elif(totalCount % 3 == 1):
    output = "P"
else:
    output = "S"