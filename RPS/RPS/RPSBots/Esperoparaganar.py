import random
if input == "":
	turn = 1
	jugadas = []
	patrones = {}
	output = "P"
else :
	output = random.choice(["R","S","P"])
	if len(jugadas) == 3:
		patron = tuple(jugadas)
		if patron not in patrones:
			patrones[patron] = {"R":0,"P":0,"S":0}
		patrones[patron][input] += 1
	jugadas.append(input+output)
	if len(jugadas) > 3:
		jugadas.pop(0)
	turn += 1
	if turn > 900:
		if patron in patrones:
			prediccion = patrones[patron]
			r = prediccion["R"]
			s = prediccion["S"]
			p = prediccion["P"]
			if r >= s and r >= p:
				output = "P"
			if s >= r and s >= p:
				output = "R"
			if p >= r and p >= s:
				output = "S"