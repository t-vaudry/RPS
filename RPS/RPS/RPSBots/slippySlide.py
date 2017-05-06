import math, random

if not input:
	myChoice = random.choice(["R","P","S"])
	strats = [[2,5,5,5],[2,5,5,5],[2,5,5,5]]
	beat={'R':'P','P':'S','S':'R'}
	newStrat = 0
	newOut = 2
	rStrat = None
	cnt = 1
	stratTot = 0
	wins = 0
	losses =0

else:
	cnt+=1
	prevStrat = newStrat
	prevOut = newOut
	if input == myChoice:
		newOut = 2;
	elif beat[input] == myChoice:
		strats[prevOut][prevStrat] += 1 + (float(stratTot) * .03);
		wins += 1
		if  not rStrat is None:
			strats[prevOut][rStrat] += 1 ;
		newOut = 0;
	else:
		newOut = 1;

	if beat[myChoice] == input:
		losses +=1

	stratTot = strats[newOut][0]+strats[newOut][1]+strats[newOut][2]+strats[newOut][3]
	selectionRND = random.randint(1,100);
	forTot = 0
	for indx in range(0,4):
		newPct = int(float(strats[newOut][indx]) / stratTot * 100)
		if selectionRND >= forTot and selectionRND < forTot + (newPct):
			newStrat = indx
		forTot += newPct

	wlp = float(wins/(losses+wins+1))*100 > float(losses/(losses+wins+1))*100

	if cnt < 700:
		newStrat = 0
	elif ( cnt > 800 and wlp > 8) :
		newStrat = 0

	if newStrat == 0:
		newChoice = random.choice(["R","P","S"])
		if not prevOut == 2:
			if newChoice == myChoice:
				rStrat = 2
			elif newChoice == input:
				rStrat = 1
			elif newChoice == beat[input]:
				rStrat = 0
			else:
				rStrat = None
		myChoice = newChoice
	elif  newStrat == 1:
		myChoice = input
	elif  newStrat == 2:
		myChoice == myChoice;
	elif  newStrat == 3:
		myChoice = beat[input];
output = myChoice