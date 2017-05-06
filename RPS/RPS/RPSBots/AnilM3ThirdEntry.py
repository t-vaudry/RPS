import random
myLast = "";
#gameCount = 0;
if input == "": # initialize variables for the first round
	RaP = RaS = RaR = 0
	PaP = PaS = PaR = 0
	SaP = SaS = SaR = 0
	PC = RC = SC = 0
elif input == "R":
	RC += 1
	if myLast == "R": 
		RaR += 1
	elif myLast == "S": 
		RaS += 1
	elif myLast == "P":
		RaP += 1
elif input == "P":
	PC += 1
	if myLast == "R": 
		PaR += 1
	elif myLast == "S": 
		PaS += 1
	elif myLast == "P":
		PaP += 1
elif input == "S":
	SC += 1
	if myLast == "R":
		SaR += 1
	elif myLast == "S":
		SaS += 1
	elif myLast == "P":
		SaP += 1
	
	
if myLast == "R":
	if RaR > PaR:
		if RaR > SaR:
			output = "P"
		else:
			output = "R"
	else:
		if PaR > SaR:
			output = "S"
		else:
			output = "R"
elif myLast == "S":
	
	if RaS > PaS:
		if RaS > SaS:
			output = "P"
		else:
			output = "R"
	else:
		if PaS > SaS:
			output = "S"
		else:
			output = "R"
elif myLast == "P":
	
	if RaP > PaP:
		if RaP > SaP:
			output = "P"
		else:
			output = "R"
	else:
		if PaP > SaP:
			output = "S"
		else:
			output = "R"
else:
	output = random.choice(["R","P","S"])
	
myLast = output
#gameCount += 1