#Testing
import random,operator

if input == "":
	rps = ["R", "P", "S"]
	beat = {'P': 'S', 'S': 'R', 'R': 'P'}
	beat2 = {'PP': 'S', 'SS': 'R', 'RR':'P', 'PS': 'S', 'PR': 'P', 'RS': 'R', 'RP': 'P', 'SP': 'S', 'SR': 'R'}
	roundsPlayed = 0
	OH =""
	MH =""
	output = random.choice(rps)
	w = 0
	moves= {"a" : "R", "b" : "P", "c" : "s", "d" : "R", "e" : "P", "f" : "S"}
	strategy = {"a" : w, "b" : w, "c" : w, "d" : w, "e" : w, "f" : w}
	C = "d"
else:
	roundsPlayed+=1
	for strat in "abcdef":
		if moves[strat] == beat[input]:
			strategy[strat] +=3
		else:
			strategy[strat] -=1
	p = [1,1]
	r = [1,1]
	s = [1,1]	
	OH += input
	MH += output
	for i in range(0, 12):
		r = [r[0]+OH.count(OH[-i:]+"R"),r[1]+MH.count(MH[-i:]+"R")]
		p = [p[0]+OH.count(OH[-i:]+"P"),p[1]+MH.count(MH[-i:]+"P")]
		s = [s[0]+OH.count(OH[-i:]+"S"),s[1]+MH.count(MH[-i:]+"S")]
	DIFF = {"RR": r[0]-r[1], "PP" : p[0]-p[1], "SS" : s[0]-s[1],"RP": r[0]-p[1],"RS":r[0]-s[1],"PS":p[0]-s[1],"PR" : p[0]-r[1],"SR" : s[0]-r[1], "SP" : s[0]-p[1]}
	PROD = {"RR": r[0]*r[1], "PP" : p[0]*p[1], "SS" : s[0]*s[1],"RP": r[0]*p[1],"RS":r[0]*s[1],"PS":p[0]*s[1],"PR" : p[0]*r[1],"SR" : s[0]*r[1], "SP" : s[0]*p[1]}
	moves["a"] = beat2[max(DIFF.iteritems(), key=operator.itemgetter(1))[0]]
	moves["b"] = beat2[min(DIFF.iteritems(), key=operator.itemgetter(1))[0]]
	moves["c"] = beat[beat2[moves["a"]+moves["b"]]]
	moves["d"] = beat2[max(PROD.iteritems(), key=operator.itemgetter(1))[0]]
	moves["e"] = beat2[min(PROD.iteritems(), key=operator.itemgetter(1))[0]]
	moves["f"] = beat[beat2[moves["d"]+moves["e"]]]
	if not(roundsPlayed%7):
		C = max(strategy.iteritems(), key=operator.itemgetter(1))[0]		
	output = moves[C]