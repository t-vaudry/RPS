import random
if not input:
	lloutput = 'P'
	loutput = output = 'P'
else:
	if input == {'R':'P','P':'S','S':'R'}[lloutput]:
		output = {'R':'S','P':'R','S':'P'}[loutput]
	elif input == {'R':'S','P':'R','S':'P'}[lloutput]:
		output = {'R':'R','P':'P','S':'S'}[loutput]
	elif input == {'R':'R','P':'P','S':'S'}[lloutput]:
		output = {'R':'P','P':'S','S':'R'}[loutput]
lloutput = loutput
loutput = output