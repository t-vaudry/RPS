import random
mossev=["RPS","PSR","SRP"]
mosse=mossev[random.randint(0,2)]
if not input:
	output =mosse[random.randint(0,2)]
else:
	if input == "R": output="R"
	if input == "P": output="P"
	if input == "S": output="S"	

if random.randint(1,10)>1: 
	output=mosse[random.randint(0,2)]