import math, random

if not input:
	myChoice = random.choice(["R","P","S"])
	strats = [[5,5,5,5],[5,5,5,5],[5,5,5,5]]
	beat={'R':'P','P':'S','S':'R'}
	newStrat = 0
	newOut = 2
else:

	prevStrat = newStrat
	prevOut = newOut
	if input == myChoice:
		newOut = 2;
	elif beat[input] == myChoice:
		if prevStrat == 0:
			strats[prevOut][prevStrat] +=1;
		else:
			strats[prevOut][prevStrat] +=3;
		newOut = 0;
	else:
		newOut = 1;

	stratTot = strats[newOut][0]+strats[newOut][1]+strats[newOut][2]+strats[newOut][3]
	selectionRND = random.randint(1,100);
	forTot = 0
	for indx in range(0,3):
		newPct = strats[newOut][indx] / stratTot * 100
		if selectionRND >= forTot and selectionRND < forTot + (newPct):
			newStrat = indx
		forTot += newPct

	if newStrat == 0:
		myChoice =random.choice(["R","P","S"]);
	elif  newStrat == 1:
		myChoice = input
	elif  newStrat == 2:
		myChoice == myChoice;
	elif  newStrat == 3:
		myChoice = beat[input];
output = myChoice