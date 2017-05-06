import random

#Select the choice that minimizes the loss count release 2

if (input == ""):
	rLoss = 0;
	sLoss = 0;  
	pLoss = 0;
	oldOutput = "R";

if ((input == "R") and (oldOutput == "S")):
	sLoss += 1;

if ((input == "S") and (oldOutput == "P")):
	pLoss += 1;

if ((input == "P") and (oldOutput == "R")):
	rLoss += 1;

if ((input == "R") and (oldOutput == "R")):
	rLoss += 1;

if ((input == "S") and (oldOutput == "S")):
	sLoss += 1;

if ((input == "P") and (oldOutput == "P")):
	pLoss += 1;


if (rLoss < sLoss) and (rLoss < pLoss):
	output = "R";
	oldOutput = "R";

elif (pLoss < sLoss) and (pLoss < rLoss):
	output = "P";
	oldOutput = "P";

elif (sLoss < pLoss) and (sLoss < rLoss):
	output = "S";
	oldOutput = "S";
else:
	output = random.choice(["R","P","S"]);
	oldOutput = output;