if input == "":
	lastR = lastP = lastS = 0
elif input == "R":
	lastR = 0
	lastP += 1
	lastS += 1
elif input == "P":
	lastP = 0
	lastR += 1
	lastS += 1
elif input == "S":
	lastS = 0
	lastR += 1
	lastP += 1
if lastR > lastP and lastR > lastS:
	output = "R"
elif lastS > lastP:
	output = "S"
else:
	output = "P"