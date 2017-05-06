from random import choice, randint
choice = ["R","P","S"]
stopRand = 60
patternMax = 5
patternAct = 0
global rCH
global pCH
global sCH

rCH = 0
pCH = 0
sCH = 0

def seqPatrn(i,z):
	global rCH
	global pCH
	global sCH
	
	if inStore[0][n - i] == inStore[0][len(inStore[0]) - (1 + i)]:
		if   inStore[0][n + 1] == choice[0]:
			rCH += 1
			pCH -= 1
		elif inStore[0][n + 1] == choice[1]:
			pCH += 1
			sCH -= 1
		elif inStore[0][n + 1] == choice[2]:
			rCH -= 1
			sCH += 1
		if i < z:
			return seqPatrn(i + 1, z)
		else:
			return
			
def selfPatrn (i,z):
	global rCH
	global pCH
	global sCH
	
	if inStore[1][n - i] == inStore[1][len(inStore[1]) - (1 + i)]:
		if   inStore[1][n + 1] == choice[0]:
			sCH -= 1
			pCH += 1
		elif inStore[1][n + 1] == choice[1]:
			rCH -= 1
			sCH += 1
		elif inStore[1][n + 1] == choice[2]:
			pCH -= 1
			rCH += 1
		if i < z:
			return selfPatrn(i + 1, z)
		else:
			return

if input == "":
	output = choice[randint(0,2)]
	matchCount = 0
	inStore = [[],[]]
elif input != "":
	inStore[0].append(input)
	inStore[1].append(output)
	
	if (len(inStore[0]) - 1) >= stopRand:
		del inStore[0][0]
		del inStore[1][0]
	
	output = ""
	
	if len(inStore[0]) < patternMax:
		patternAct = (len(inStore[0]) - 1)
	else:
		patternAct = patternMax
	 
	if matchCount < stopRand:
		output = choice[randint(0,2)]
	else:
		
		
		for n in range(len(inStore[0]) - 1):
			seqPatrn(0,patternAct)
			selfPatrn(0,patternAct)
		
			if   (rCH >  pCH) and (rCH >  sCH):
				output = choice[1]
			elif (pCH >  rCH) and (pCH >  sCH):
				output = choice[2]
			elif (sCH >  rCH) and (sCH >  pCH):
				output = choice[0]
			elif (sCH == rCH) and (sCH >  pCH):
				output = choice[(randint(0,1) * 2)]
			elif (sCH == pCH) and (sCH >  rCH):
				output = choice[randint(1,2)]
			elif (rCH == pCH) and (rCH >  sCH):
				output = choice[randint(0,1)]
			elif (sCH == rCH) and (sCH == pCH):
				output = choice[randint(0,2)]
			else:
				output = choice[randint(0,2)]
			
matchCount += 1