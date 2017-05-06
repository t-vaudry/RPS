import random
if len(input) < 2:
	output = random.choice(["R","P","S"])
else:
	d = dict()
	d["RR"] = d["RP"] = d["RS"] = 0
	d["PR"] = d["PP"] = d["PS"] = 0
	d["SR"] = d["SP"] = d["SS"] = 0
	for i in xrange(len(input)-1):
		d[input[i:i+2]]+=1
	lastMove = input[len(input)-1]
	mx = 0
	mxMove = lastMove
	for move in "RPS":
		if mx < d[lastMove+move]:
			mx = d[lastMove+move]
			mxMove = move
	output = {'R':'P', 'P':'S', 'S':'R'}[mxMove]