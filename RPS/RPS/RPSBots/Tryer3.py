if input == "": # initialize variables for the first round
	rC = pC = sC = 0
elif input == "R":
	rC += 1
elif input == "P":
	pC += 1
elif input == "S":
	sC += 1
if rC > pC and rC > sC:
	output = "P" # paper beats rock
elif pC > sC and pC > rC:
	output = "S" # scissors beats paper
elif sC > pC and sC > rC:
	output = "R" # rock beats scissors
elif rC==pC and pC==sC:
        output = "P"
elif rC==pC and sC==rC:
        output = "R"
elif pC==sC and sC==rC:
        output = "S"
elif pC==sC and pC==rC:
        if input =='R':
              output ="S"
        elif input =="S":
              output ="P"
        elif input =="P":
              output ="R"