import random
if not input:
	lloutput = 'P'
	loutput = output = 'P'
	num = 0;
else:
	if num<3:
		output = 'P'
		num+=1;
	elif num%3==0:
		output = random.choice(['R', 'P', 'S'])
	elif input == {'R':'P','P':'S','S':'R'}[lloutput]:
		output = {'R':'S','P':'R','S':'P'}[loutput]
	elif input == {'R':'S','P':'R','S':'P'}[lloutput]:
		output = {'R':'R','P':'P','S':'S'}[loutput]
	elif input == {'R':'R','P':'P','S':'S'}[lloutput]:
		output = {'R':'P','P':'S','S':'R'}[loutput]
lloutput = loutput
loutput = output