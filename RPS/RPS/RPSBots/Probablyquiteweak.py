if not input:
	lloutput = 'P'
	loutput = output = 'P'
	linput = 'P'
	num = 0;
else:
	if num<3:
		output = 'P'
	elif input == {'R':'P','P':'S','S':'R'}[linput]:
		output = {'R':'S','P':'R','S':'P'}[input]
	elif input == {'R':'S','P':'R','S':'P'}[linput]:
		output = {'R':'R','P':'P','S':'S'}[input]
	elif input == {'R':'R','P':'P','S':'S'}[linput]:
		output = {'R':'P','P':'S','S':'R'}[input]
lloutput = loutput
loutput = output
num+=1
linput = input