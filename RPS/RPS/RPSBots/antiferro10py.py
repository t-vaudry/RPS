#email: putiferio61@gmail.com
import random
if not input:
	#print "not input"
	mossed=["RPS","PSR","SRP"]
	mosse=mossed[random.randint(0,2)]
	mappa={"R":0,"P":1,"S":2}
	inversa={0:"R",1:"P",2:"S"}
	conta=[3.,3.,3.]
	output =mosse[random.randint(0,2)]
else:
	conta[mappa[output]]=conta[mappa[output]]+1.
	conta[0] = conta[0]*0.95+.0001*random.random()
	min = conta[0]
	output = inversa[0]
	for i in range(1,3):
		conta[i]=conta[i]*0.95+.0001*random.random()
		if conta[i]<min:
			min = conta[i]
			output = inversa[i]
if random.randint(1,10)>1: 
	output=mosse[random.randint(0,2)]