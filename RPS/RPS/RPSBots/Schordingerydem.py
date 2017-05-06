import random
if input == "":
	patrones = {}
	cola = []
	output = "R"
else:
	cola.append(input)
	if len(cola) == 8:
		cola.pop(0)
	for i in xrange(1, len(cola)-1):
		patron = tuple(cola[len(cola)-i-1:len(cola)-1])
		if patron in patrones:
			if input in patrones[patron]:
				patrones[patron][input] += 1
			else :
				patrones[patron][input] = 1
		else :
			patrones[patron] = {}
			patrones[patron][input] = 1
	if tuple(cola) in patrones:
		rocks = patrones[tuple(cola)].get("R",0)
		papers = patrones[tuple(cola)].get("P",0)
		scissors = patrones[tuple(cola)].get("S",0)
		if rocks >= papers and rocks >= scissors:
			output = "P"
		if papers >= rocks and papers >= scissors:
			output = "S"
		if scissors >= rocks and scissors >= papers:
			output = "R"
	else :
		output = random.choice(["R", "S", "P"])