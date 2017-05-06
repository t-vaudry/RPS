if input == "":
	rC = pC = sC = 0
elif input == "R":
	rC += 1
elif input == "P":
	pC += 1
elif input == "S":
	sC += 1
if rC > pC and rC > sC:
	output = "P"
elif pC > sC:
	output = "S"
else:
	output = "R"