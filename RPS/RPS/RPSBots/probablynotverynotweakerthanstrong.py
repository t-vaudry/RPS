import random
if not input:
	lloutput = loutput = output = 'P'
else:
        lloutput = loutput
        loutput = input
	if fakeinput == {'R':'P','P':'S','S':'R'}[lloutput]:
		output = {'R':'R','P':'P','S':'S'}[loutput]
	elif fakeinput == {'R':'S','P':'R','S':'P'}[lloutput]:
		output = {'R':'P','P':'S','S':'R'}[loutput]
	elif fakeinput == {'R':'R','P':'P','S':'S'}[lloutput]:
		output = {'R':'S','P':'R','S':'P'}[loutput]
fakeinput = output