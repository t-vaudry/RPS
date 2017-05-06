#email: putiferio61@gmail.com
import random
mosse="RPS"
if not input:
	mappa={"R":0,"P":1,"S":2}
	inversa={0:"R",1:"P",2:"S"}
	risultato={"RR":0,"RP":1,"RS":-1,"PR":-1,"PP":0,"PS":1,"SR":1,"SP":-1,"SS":0}
	listagiocate=""
	output =mosse[random.randint(0,2)]
	vincita1=1.
	vincita2=1.
	vincita3=1.
	n=0
else:
	n=n+1
	ultima=input+output
	listagiocate=listagiocate+input+output+"-"
	if n>3:
		vincita1=.9*vincita1+risultato[input+output1]
		if flag2==1:
			vincita2=.9*vincita2+risultato[input+output2]
		if flag3==1:
			vincita3=.9*vincita3+risultato[input+output3]
	if len(listagiocate)>102:
		listagiocate=listagiocate[3:]
	output1=inversa[(mappa[input]+1)%3]
	output2=output1
	output3=output1
	listarunning=listagiocate[:-3]
	if n>2:
		flag2=0
		flag3=0
		k=listarunning.rfind(ultima)
		if k>0:
			output2=inversa[(mappa[listagiocate[k+3]]+1)%3]
			flag2=1
			output3=inversa[(mappa[listagiocate[k+3]]+2)%3]
			flag3=1
	if vincita1>vincita2:
		output=output1
		max=vincita1
	else:
		output=output2
		max=vincita2
	if vincita3>max:
		output=output3
if random.randint(1,10)>1: 
	output=mosse[random.randint(0,2)]