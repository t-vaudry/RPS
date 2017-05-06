#email: putiferio61@gmail.com
import random
mossed=["RPS","PSR","SRP"]
mosse=mossed[random.randint(0,2)]
vincitad={"RR":0,"RP":-1,"RS":1,"PR":1,"PP":0,"PS":-1,"SR":-1,"SP":1,"SS":0}
mappa={"R":0,"P":1,"S":2}
inversa={0:"R",1:"P",2:"S"}
strategia0={"R":"P","P":"S","S":"R"}
strategia1={"R":"R","P":"P","S":"S"}
changestrategy=0
conta=[3.,3.,3.]
flag=0

if not input:
	strategia=strategia0
	n=0
	v=0
	#print "not input"
	stringa = ""
	output =mosse[random.randint(0,2)]
else:
	flag=1
	outputold = output
	n=n+1
	conta[mappa[input]]=conta[mappa[input]]+1.
	conta[0] = conta[0]*0.87+.0001*random.random()
	min = conta[0]
	output = inversa[0]
	for i in range(1,3):
		conta[i]=conta[i]*0.87+.0001*random.random()
		if conta[i]<min:
			min = conta[i]
			output = inversa[i]
	if changestrategy==1:
		output=strategia0[input]
		#print "input = ",input
	#output=strategia[input]

if random.randint(1,10)>1: 
	output=mosse[random.randint(0,2)]
	flag=0

if flag==1:
	giocate=outputold+input
	v = vincitad[giocate]+v