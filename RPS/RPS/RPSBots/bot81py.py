#email: putiferio61@gmail.com
import random
mosse="RPS"
alfa=.9
if not input:
	tryoutput=["R"]*4
	mappa={"R":0,"P":1,"S":2}
	inversa={0:"R",1:"P",2:"S"}
	risultato={"RR":0,"RP":1,"RS":-1,"PR":-1,"PP":0,"PS":1,"SR":1,"SP":-1,"SS":0}
	markovoutput=[[1] * 3 for x in range(9)]
	markovinput=[[1] * 3 for x in range(9)]
	output =mosse[random.randint(0,2)]
	vincita=[0]*3
	n=0
else:
	#controllare la definizione di ultima per n bassi
	n=n+1
	if n==2:
		ultima=mappa[input]+3*mappa[output]
		output =mosse[random.randint(0,2)]
	if n>2:
		penultima = ultima
		ultima=mappa[input]+3*mappa[output]
		for i in range(0,9):
			for j in range(0,3):
				markovoutput[i][j]=alfa*markovoutput[i][j]
				markovinput[i][j]=alfa*markovinput[i][j]
		markovinput[penultima][mappa[input]]=markovinput[penultima][mappa[input]]+1.
		markovoutput[penultima][mappa[output]]=markovoutput[penultima][mappa[output]]+1.
	if n>3:
		for i in range(0,3):
			stringa = input+tryoutput[i]
			vincita[i]=alfa*vincita[i]+risultato[stringa] #manca l'input al risultato
	tryoutput[0]=inversa[(mappa[input]+1)%3]
	if n>2:
		listainput=markovinput[ultima]
		#print listainput
		#print listainput[1]
		listaoutput=markovoutput[ultima]
		for i in range(0,3):
			listainput[i]=listainput[i]+0.000001*random.random()
			listaoutput[i]=listaoutput[i]+0.000001*random.random()
		maxinput=max(listainput)
		maxoutput=max(listaoutput)
		maxinputindex = listainput.index(maxinput)
		maxoutputindex = listaoutput.index(maxoutput)
		tryoutput[1]=inversa[(maxinputindex+1)%3]
		tryoutput[2]=inversa[(maxinputindex+2)%3]
		tryoutput[3]=inversa[(maxoutputindex+2)%3]
		vincitamax=max(vincita)
		vincitamaxindex=vincita.index(vincitamax)
		output=tryoutput[vincitamaxindex]
		if max<0:
			output=mosse[random.randint(0,2)]
if random.randint(1,14)>1: 
	output=mosse[random.randint(0,2)]