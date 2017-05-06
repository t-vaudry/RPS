import random

if input != "R" or "P" or "S":
	rockCount = 0
	paperCount = 0
	scissorsCount = 0
	myMoves = []
	opMoves = []
	bothMoves = []
	opNextMoveLst = []

	output = random.choice(["R", "P", "S"])

else:
	myMoves.append(output)
	opMoves.append(input)
	bothMoves.append(output + input)
	strBoth = output + input
	checkBoth = [i for i, x in enumerate(bothMoves) if x == strBoth]
	if checkBoth != []:
		for playMatch in checkBoth:
			nextMove = playMatch+1
			opNextMove = opMoves[nextMove]
			opNextMoveLst.append(opNextMove)
		opNmStr = "".join(opNextMoveLst)
		opRMvs = opNmStr.count("R")
		opSMvs = opNmStr.count("S")
		opPMvs = opNmStr.count("P")
		if opRMvs > opPMvs and opRMvs > opSMvs:
			output = "P"
		elif opPMvs > opSMvs:
			output = "S"
		else:
			output = "R"
	elif len(opMoves) >= 2:
		checkOp = [i for i, x in enumerate(opMoves) if x == input]
		for playMatch in checkOp:
			nextMove = playMatch+1
			opNextMove = opMoves[nextMove]
			opNextMoveLst.append(opNextMove)
		opNmStr = "".join(opNextMoveLst)
		opRMvs = opNmStr.count("R")
		opSMvs = opNmStr.count("S")
		opPMvs = opNmStr.count("P")
		if opRMvs > opPMvs and opRMvs > opSMvs:
			output = "P"
		elif opPMvs > opSMvs:
			output = "S"
		else:
			output = "R"

	else:
		output = random.choice(["R", "P", "S"])