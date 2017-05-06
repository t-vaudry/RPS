import random

if input != "R" or "P" or "S":
	rockCount = 0
	paperCount = 0
	scissorsCount = 0
	myMoves = []
	opMoves = []
	bothMoves = []
	opNextMoveLst = []
	losses = 0

	output = random.choice(["R", "P", "S"])

else:
	if (input == "R" and output == "S") or (input == "P" and output == "R") or (input == "S" and output == "P"):
		losses=losses+1
		pass
	else:
		losses = 0
		pass
	myMoves.append(output)
	opMoves.append(input)
	bothMoves.append(output + input)
	strBoth = output + input
	opRMvs = ""
	opSMvs = ""
	opPMvs = ""
	opNmStr = ""
	checkBoth = [i for i, x in enumerate(bothMoves) if x == strBoth]
	if losses >= 4:
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
				output = "S"
			elif opPMvs > opSMvs:
				output = "R"
			else:
				output = "P"
		elif checkBoth == [] and len(opMoves) < 20:
			opMvStr = "".join(opMoves)
			opRMvs = opMvStr.count("R")
			opSMvs = opMvStr.count("S")
			opPMvs = opMvStr.count("P")
			if opRMvs > opPMvs and opRMvs > opSMvs:
				output = "P"
			elif opPMvs > opSMvs:
				output = "S"
			else:
				output = "R"

		elif len(opMoves) >= 20:
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
				output = "S"
			elif opPMvs > opSMvs:
				output = "R"
			else:
				output = "P"
		else:
			output = random.choice(["R", "P", "S"])

	elif checkBoth != []:
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