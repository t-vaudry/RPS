#!/usr/bin/env python

import random

opciones = ["S","R","P"]
vencedores = {'S':'R','R':'P','P':'S'}
tabla = {'S':1,'R':1,'P':1}

def actualizarTabla(output):
	tabla[output] += 1

def dameMaximo():
	maximo = 0
	dato = ""
	for k,v in tabla.items():
		if v > maximo:
			maximo = v
			dato = k
	return dato
	
def evitarPrediccion():
	v1 = vencedores[dameMaximo()]
	return vencedores[v1]

if (input == ""):
	output = random.choice(opciones)
else:
	if(input == vencedores[output]):			
		actualizarTabla(input)
		output = evitarPrediccion()
	else:
		actualizarTabla(input)
		output = vencedores[dameMaximo()]