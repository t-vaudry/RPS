import random

if input == "":
	strat = 2 #strats: 0 = beat op last, 1 = beat my last, 2 = 3rd order rfind, 3 = random
	win0 = 100
	win1 = 100
	win2 = 100
	win3 = 100
	history = ""
	_out = random.choice(["R", "P", "S"])
	hiscap = 200
else:
	history += input
	if len(history) > hiscap:
		history = history[1:]
		
	if strat == 0:
		if input == "R":
			if _out == "S":
				win0 -= 1
			if _out == "P":
				win0 += 1
		if input == "S":
			if _out == "P":
				win0 -= 1
			if _out == "R":
				win0 += 1
		if input == "P":
			if _out == "R":
				win0 -= 1
			if _out == "S":
				win0 += 1
		if win0 > 100:
			win0 = 100
	
	if strat == 1:
		if input == "R":
			if _out == "S":
				win1 -= 1
			if _out == "P":
				win1 += 1
		if input == "S":
			if _out == "P":
				win1 -= 1
			if _out == "R":
				win1 += 1
		if input == "P":
			if _out == "R":
				win1 -= 1
			if _out == "S":
				win1 += 1
		if win1 > 100:
			win1 = 100
	
	if strat == 2:
		if input == "R":
			if _out == "S":
				win2 -= 1
			if _out == "P":
				win2 += 1
		if input == "S":
			if _out == "P":
				win2 -= 1
			if _out == "R":
				win2 += 1
		if input == "P":
			if _out == "R":
				win2 -= 1
			if _out == "S":
				win2 += 1
		if win2 > 100:
			win2 = 100
			
	if strat == 3:
		if input == "R":
			if _out == "S":
				win3 -= 1
			if _out == "P":
				win3 += 1
		if input == "S":
			if _out == "P":
				win3 -= 1
			if _out == "R":
				win3 += 1
		if input == "P":
			if _out == "R":
				win3 -= 1
			if _out == "S":
				win3 += 1
		if win3 > 100:
			win3 = 100
	
	if win0 < 50:
		strat = 1
	if win1 < 50:
		strat = 3
	if win2 < 50:
		strat = 0

	if strat == 0:
		oplast = history[len(history)-1:]
		if oplast == "R":
			_out = "P"
		if oplast == "S":
			_out = "R"
		if oplast == "P":
			_out = "S"
	if strat == 1:
		if _out == "R":
			_out = "P"
		elif _out == "S":
			_out = "R"
		elif _out == "P":
			_out = "S"
	if strat == 2:
		if len(history) >= 3:
			search = history[:3]
			mplace = history.rfind(search)
			predict = history[mplace+1]
			if predict == "R":
				_out = "P"
			elif predict == "P":
				_out = "S"
			elif predict == "S":
				_out = "R"
			else:
				_out = random.choice(["R","P","S"])
		else:
			_out = random.choice(["R","P","S"])
	if strat == 3:
		_out = random.choice(["R", "P", "S"])

output = _out