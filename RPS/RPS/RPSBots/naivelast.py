import random
pastFreq = {}
lastThrow = "R"
winningThrows = {"R":"P", "P":"S", "S":"R"}
pastFreq = {"R": {"R":0, "P":0, "S":0}, "P": {"R":0, "P":0, "S":0}, "S": {"R":0, "P":0, "S":0}}

if input == "":
	output = random.choice(["R","P","S"])
	lastThrow = output
else:
	pastFreq[lastThrow][input] += 1
	lastThrowStats = pastFreq[lastThrow]
	probR = lastThrowStats["R"]
	probP = lastThrowStats["P"]
	probS = lastThrowStats["S"]
	likelyNext = "R"
	if probP >= probR and probP >= probS:
		likelyNext = "P"
	elif probS >= probR and probS >= probP:
		likelyNext = "S"
	output = winningThrows[likelyNext]
	lastThrow = output