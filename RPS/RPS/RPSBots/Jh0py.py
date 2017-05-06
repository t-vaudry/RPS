#email: putiferio61@gmail.com
import random
if not input:
	mosse="RPS"
	mappa={"R":0,"P":1,"S":2}
	inversa={0:"R",1:"P",2:"S"}
	alfa=0.85
	a=1./(1.-alfa)
	b=a
	A=0.1
	B=-1.
	C=-0.1
	D=.3
	conta=[a,a,a]
	contamarkovlui=[[b,b,b],[b,b,b],[b,b,b]]
	contamarkovio=[[b,b,b],[b,b,b],[b,b,b]]
	output =mosse[random.randint(0,2)]
	n=0
	tempo=0
else:
	n=n+1
	if n>1:
		outputnm2=outputnm1
		inputnm2=inputnm1
		contesto=(mappa[outputnm2]-mappa[inputnm2])%3
		giocatalui=(mappa[input]-mappa[inputnm2])%3
		giocataio=(mappa[output]-mappa[inputnm2])%3
		for i in range(0,3):
			for j in range(0,3):
				contamarkovlui[i][j]=contamarkovlui[i][j]*alfa
				contamarkovio[i][j]=contamarkovio[i][j]*alfa
		contamarkovlui[contesto][giocatalui]=contamarkovlui[contesto][giocatalui]+1.
		contamarkovio[contesto][giocataio]=contamarkovlui[contesto][giocataio]+1.
	outputnm1=output
	inputnm1=input
	for i in range(0,3):
		conta[i]=conta[i]*alfa
	conta[mappa[outputnm1]]=conta[mappa[outputnm1]]+1.
	output=mosse[random.randint(0,2)]
	if n>1:
		contestorunning=(mappa[outputnm1]-mappa[inputnm1])%3
		veclui=contamarkovlui[contestorunning]
		vecio=contamarkovio[contestorunning]
		p0lui=veclui[mappa[inputnm1]]
		p1lui=veclui[(mappa[inputnm1]+1)%3]
		p2lui=veclui[(mappa[inputnm1]+2)%3]
		p0io=B*vecio[mappa[inputnm1]]+C*conta[0]+A*p2lui+0.0001*random.random()
		p1io=B*vecio[(mappa[inputnm1]+1)%3]+C*conta[1]+A*p0lui+0.0001*random.random()
		p2io=B*vecio[(mappa[inputnm1]+2)%3]+C*conta[2]+A*p1lui+0.0001*random.random()
		if inputnm1=="R": 
			pRio=p0io
			pPio=p1io
			pSio=p2io
		if inputnm1=="P": 
			pPio=p0io
			pSio=p1io
			pRio=p2io
		if inputnm1=="S": 
			pSio=p0io
			pRio=p1io
			pPio=p2io
		max=pRio
		output="R"
		if (pPio>max):
			max=pPio
			output="P"
		if (pSio>max):
			max=pSio
			output="S"
	if random.randint(tempo,100)>10: 
		output=mosse[random.randint(0,2)]
		tempo=tempo-1
		if tempo<11:
			tempo=0
	else:
		tempo=15