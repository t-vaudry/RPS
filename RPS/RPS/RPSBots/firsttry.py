import random
import math

def normpdf(x, mean, sd):

    var = float(sd)
    pi = 3.1415926
    denom = (2*pi*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom

if input == "" :
		rockCount  = paperCount = scissorCount = matchCount = 0
		startBayes = 100
elif input == "R":
		rockCount += 1
elif input == "S":
		scissorCount += 1
elif input == "P":
		paperCount += 1

if matchCount <= startBayes :
	matchCount += 1;
	output = random.choice(["R","P","S"])		
else :
		mean  = float((1 * rockCount + 2 * paperCount + 3 * scissorCount) /  matchCount)
		variance = float((pow(1 - mean,2) + pow (2 - mean,2) + pow(3 - mean,2) ) / matchCount)
		
		matchCount += 1;
		
		probRock = normpdf(1,mean,variance)
		probPaper = normpdf(2,mean,variance)
		probScissor = normpdf(3,mean,variance)
		
		maxProb = max(probPaper,probRock,probScissor)
		
		if maxProb == probPaper :
				output = "P"
		elif maxProb == probRock :
				output = "R"
		elif maxProb == probScissor :
				output = "S"
		else :
			output = random.choice(["R","P","S"])