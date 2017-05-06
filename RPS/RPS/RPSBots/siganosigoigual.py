import random

jugadaAnteriorDelRival = input

if input == "":
	miJugadaAnterior = ""

def ganarleA(jugada):
	
	if jugada == "":
		return random.choice(["R","P","S"])
	
	elif jugada == "R":
		return "P"
	
	elif jugada == "P":
		return "S"
		
	else:
		return "R"
		
def heGanadoLaAnterior():

	return miJugadaAnterior == ganarleA(jugadaAnteriorDelRival)

if heGanadoLaAnterior():
	output = miJugadaAnterior
else:
	output = ganarleA(jugadaAnteriorDelRival)

miJugadaAnterior = output