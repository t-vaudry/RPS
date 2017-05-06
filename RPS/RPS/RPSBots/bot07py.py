#putiferio61@gmail.com
import random
mossev=["RPS","PSR","SRP"]
mosse=mossev[random.randint(0,2)]
if not input:
	output =mosse[random.randint(0,2)]
else:
	if input == "R": output="P"
	if input == "P": output="S"
	if input == "S": output="R"	

if random.randint(1,12)>1: 
	output=mosse[random.randint(0,2)]