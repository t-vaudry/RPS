import random


p = 1
r = 2
s = 3

count = 1
sum = 0
sampleSize=10
average=0
diffAvgS = diffAvgP = diffAvgR = 0

if input == "": # initialize variables for the first round
	rockCount = paperCount = scissorsCount = 0
elif input == "R":
	rockCount +=r
elif input == "P":
	paperCount +=p
elif input == "S":
	scissorsCount +=s

if rockCount>0 and scissorsCount>0 and paperCount>0:
	average=((rockCount+paperCount+scissorsCount)/count)
elif rockCount>0 and scissorsCount>0:
	average=((rockCount+scissorsCount)/count)
elif rockCount>0 and paperCount>0:
	average=((rockCount+paperCount)/count)
elif paperCount>0 and scissorsCount>0:
	average=((paperCount+scissorsCount)/count)
elif paperCount>0:
	average=(paperCount/count)
elif scissorsCount>0:
	average=(scissorsCount/count)
elif rockCount>0:
	average=(rockCount/count)

diffAvgS = abs(average-scissorsCount)
diffAvgP = abs(average-paperCount)
diffAvgR = abs(average-rockCount)

if diffAvgR<diffAvgS and diffAvgR<diffAvgP: # r=s r=p p=s
			output = "P"
elif diffAvgP<diffAvgS and diffAvgP<diffAvgR:
			output = "S"
elif diffAvgS<diffAvgR and diffAvgS<diffAvgP:
			output = "R"
elif diffAvgS==diffAvgR:
			output = "P"
elif diffAvgS==diffAvgR and diffAvgR==diffAvgP:
			output = random.choice(["R","P","S"])	
if diffAvgS==diffAvgR and diffAvgR<diffAvgS:
			output = "S"
else:
			output = "R"
if diffAvgP==diffAvgR and diffAvgR<diffAvgS:
			output = "S"
else:
			output = "R"	
if diffAvgS==diffAvgP and diffAvgP<diffAvgR:
			output = "R"
else:
			output = "P"


count = count + 1
rockCount = 0
paperCount = 0
scissorsCount = 0