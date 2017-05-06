import random

recordOutput = True

#print "input was " + input
if input=='': #first round; initialize everything
	roundNum = 0
	lastN = ['R','S','R','P','P']
	myLastMove = 'X'
else:
	roundNum += 1
	lastN.append(input)


if recordOutput:
	print "Round " + str(roundNum) + ": " + myLastMove + input

#s = 'RPS'
#output = s[(roundNum*roundNum)%3]
#choose output based on current value
if random.random() < 0.8:
	output = lastN.pop(0)
else:
	output = lastN[4]

myLastMove = output