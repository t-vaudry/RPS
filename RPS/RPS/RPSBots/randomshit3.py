import random
if not input:
	lloutput = loutput = output = 'R'
else:
        lloutput = loutput
        loutput = input
	if fakeinput == {'R':'P','P':'S','S':'R'}[lloutput]:
		output = {'R':'R','P':'P','S':'S'}[loutput]
	elif fakeinput == {'R':'S','P':'R','S':'P'}[lloutput]:
		output = {'R':'P','P':'S','S':'R'}[loutput]
	elif fakeinput == {'R':'R','P':'P','S':'S'}[lloutput]:
		output = {'R':'S','P':'R','S':'P'}[loutput]
r = random.randrange(0,3)
if r==2:
        move = random.randrange(0,3)
	if move == 1:
		output = "R"
	elif move == 2:
		output = "P"
	else:
		output = "S"
elif r==3:
        output = "R"
fakeinput = output