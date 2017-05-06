import random
mossev=["RPS","PSR","SRP"]
mosse=mossev[random.randint(0,2)]
strategia={"RR":"P","PR":"R","SR":"P","RP":"S","PP":"S","SP":"P","RS":"S","PS":"R","SS":"R"}
if not input:
	output =mosse[random.randint(0,2)]
else:
	giocata=output+input
	output=strategia[giocata]
if random.randint(1,10)>1: 
	output=mosse[random.randint(0,2)]