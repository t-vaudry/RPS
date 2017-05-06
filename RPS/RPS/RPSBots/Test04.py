import random

#Select the choice that minimizes the loss count

if (input == ""):
	rLoss = 0;
	sLoss = 0;  
	pLoss = 0;

if ((input == "R") and (output == "S")):
	sLoss += 1;

if ((input == "S") and (output == "P")):
	pLoss += 1;

if ((input == "P") and (output == "R")):
	rLoss += 1;

if (rLoss < sLoss) and (rLoss < pLoss):
	output = "R";
elif (pLoss < sLoss) and (pLoss < rLoss):
	output = "P";
elif (sLoss < pLoss) and (sLoss < rLoss):
	output = "S";
else:
	output = "R";