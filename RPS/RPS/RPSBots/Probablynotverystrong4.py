if not input:
	lloutput = 'P'
	input = predict1 = predict2 = loutput = output = 'P'
	predictor = 1
else:
	if oldpredict1==input:
		predictor = 1
	else:
		predictor = 2
	if input == {'R':'P','P':'S','S':'R'}[lloutput]:
		predict1 = {'R':'P','P':'S','S':'R'}[loutput]
	elif input == {'R':'S','P':'R','S':'P'}[lloutput]:
		predict1 = {'R':'S','P':'R','S':'P'}[loutput]
	elif input == {'R':'R','P':'P','S':'S'}[lloutput]:
		predict1 = {'R':'R','P':'P','S':'S'}[loutput]
	if input == {'R':'P','P':'S','S':'R'}[linput]:
		predict1 = {'R':'P','P':'S','S':'R'}[input]
	elif input == {'R':'S','P':'R','S':'P'}[linput]:
		predict1 = {'R':'S','P':'R','S':'P'}[input]
	elif input == {'R':'R','P':'P','S':'S'}[linput]:
		predict1 = {'R':'R','P':'P','S':'S'}[input]
	
	output = {1:predict1,2:predict2}[predictor]
lloutput = loutput
loutput = output
linput = input
oldpredict1 = predict1
oldpredict2 = predict2