import random




if input == "": # initialize variables for the first round
	p = 1
	r = 2
	s = 3
	count = 1
	average = diffAvgS = diffAvgP = diffAvgR = rockCount = paperCount = scissorsCount = 0
elif input == "R":
	rockCount +=r
elif input == "P":
	paperCount +=p
elif input == "S":
	scissorsCount +=s


	
average=((rockCount+paperCount+scissorsCount)/count)

diffAvgS = abs(average-s)
diffAvgP = abs(average-p)
diffAvgR = abs(average-r)

if diffAvgR<diffAvgS and diffAvgR<diffAvgP: # r=s r=p p=s
			output = "P"
elif diffAvgP<diffAvgS and diffAvgP<diffAvgR:
			output = "S"
elif diffAvgS<diffAvgR and diffAvgS<diffAvgP:
			output = "R"
elif diffAvgS==diffAvgR and diffAvgR==diffAvgP:
			output = random.choice(["R","P","S"])	



count = count + 1