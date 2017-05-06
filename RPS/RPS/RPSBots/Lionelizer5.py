import random

if input == "": # initialize variables for the first round
	rockCount = paperCount = scissorsCount = 0
elif input == "R":
	rockCount += 1
elif input == "P":
	paperCount += 1
elif input == "S":
	scissorsCount += 1

options = ["R","P","S"]

for x in xrange(0,250-rockCount/4):
	options.append("P")
	
for x in xrange(0,250-paperCount/4):
	options.append("S")

for x in xrange(0,250-scissorsCount/4):
	options.append("R")

output = random.choice(options)