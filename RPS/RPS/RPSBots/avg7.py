import random





p = 1
r = 2
s = 3
count = 1
average = 0
diffAvgS = 0
diffAvgP = 0
diffAvgR = 0
rockCount = 0
paperCount = 0
scissorsCount = 0
	
if input == "R":
	rockCount +=r
elif input == "P":
	paperCount +=p
elif input == "S":
	scissorsCount +=s


	
average=((rockCount+paperCount+scissorsCount)/count)

diffAvgS = abs(average-s)
diffAvgP = abs(average-p)
diffAvgR = abs(average-r)

if diffAvgR<diffAvgS and diffAvgR<diffAvgP:
			output = "P"
elif diffAvgP<diffAvgS and diffAvgP<diffAvgR:
			output = "S"
elif diffAvgS<diffAvgR and diffAvgS<diffAvgP:
			output = "R"
elif diffAvgS==diffAvgR and diffAvgR==diffAvgP:
			output = random.choice(["R","P","S"])	



count = count + 1