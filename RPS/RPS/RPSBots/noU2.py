import math, random

if not input:
	myChoice = "R"
	wins = 0
	losses = 0
	beat={'R':'P','P':'S','S':'R'}
else:
	if (wins + losses) == 0:
		myChoice = random.choice(["R","P","S"])
	else:
		if not (input == myChoice):
			if beat[myChoice] == input:
				wins = wins + 1;
			else:
				losses = losses + 1;
			if random.randint(1,10) == 10:
				myChoice =random.choice(["R","P","S"])
			else:
				selectionWeight = random.randint(1,100);
				if not (((wins / (wins+losses)) * 100) >= selectionWeight):
					myChoice = input;
output = myChoice