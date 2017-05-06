import random
if input == "" :
	jugadas = []
	output = "P"
	gana = {"R":"P", "S":"R", "P":"S"}
	patrones = {}
	score = 0
	beatHim = True
	round = 1

else :
    if gana[input]==output:
        score = score + 1
    if gana[output]==input:
        score = score -1
    
    if score < -30 and beatHim:
        beatHim = False
        score = 0
    if score < -30 and not beatHim:
        beatHim = True
        score = 0
            
    for k in xrange(len(jugadas)):
	patron = tuple(jugadas[k::])
	if patron not in patrones:
	    patrones[patron] = {"R":0, "S":0, "P":0}
	patrones[patron][input] += 1
    jugadas.append(output+input)
    if len(jugadas) > 5:
	jugadas.pop(0)
    k = 5
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
            if beatHim:
              output = "P" 
            else:
              output = "R"

        if papers >= rocks and papers >= scissors:
	    if beatHim:
               output = "S"
            else:
               output = "P"

        if scissors >= rocks and scissors >= papers:
            if beatHim:
               output = "R"
            else:
	       output = "S"