#email: putiferio61@gmail.com
import random
mosse="RPS"
if not input:
	mappa={"R":0,"P":1,"S":2}
	inversa={0:"R",1:"P",2:"S"}
	listagiocate=""
	output =mosse[random.randint(0,2)]
	n=0
else:
	n=n+1
	ultima=input+output
	listagiocate=listagiocate+input+output+"-"
	if len(listagiocate)>102:
		listagiocate=listagiocate[3:]
	output1=inversa[(mappa[input]+1)%3]
	output2=output1
	listarunning=listagiocate[:-3]
	if n>2:
		k=listarunning.rfind(ultima)
		if k>0:
			output2=inversa[(mappa[listagiocate[k+3]]+1)%3]
	if random.randint(0,1)==0:
		output=output1
	else:
		output=output2
if random.randint(1,10)>1: 
	output=mosse[random.randint(0,2)]