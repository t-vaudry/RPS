import random
if input == "":
	jugadas = []
	output = "P"
	gana = {"R":"P", "S":"R", "P":"S"}
	patrones = {}

else :
	for k in xrange(len(jugadas)):
		patron = tuple(jugadas[k::])
		if patron not in patrones:
			patrones[patron] = {"R":0, "S":0, "P":0}
		patrones[patron][input] += 1
	jugadas.append(output+input)
	if len(jugadas) > 10:
		jugadas.pop(0)
	k = 10
	while k >= 1 and tuple(jugadas[len(jugadas)-k: len(jugadas)]) not in patrones:
		k -= 1
	if k == 0:
		output = random.choice(["R", "S", "P"])
	else :
		prediccion = patrones[tuple(jugadas[len(jugadas)-k: len(jugadas)])]
		rocks = prediccion["R"]
		papers = prediccion["P"]
		scissors = prediccion["S"]
		if rocks >= papers and rocks >= scissors:
			output = "P"
		if papers >= rocks and papers >= scissors:
			output = "S"
		if scissors >= rocks and scissors >= papers:
			output = "R"