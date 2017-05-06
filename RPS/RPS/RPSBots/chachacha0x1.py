import random

if input == "":
	rwd = {'RR': 0, 'PP': 0, 'SS': 0, 'PR': 1, 'RS': 1, 'SP': 1,'RP': -1, 'SR': -1, 'PS': -1}
	opp = {'R': 'S', 'P': 'R', 'S': 'P'}
	rec = {"RS": [], "RP": [], "SR": [], "SP": [], "PR": [], "PS": [], "SS": [], "PP": [], "RR": []}
	
	# Discounter
	dsc = 0.999
	
	# History window
	wdw = 20
	
	# Retrospect window
	rtr = 10
	
	# History
	hst = []
	inc = 0.02
	
	counts = {"R": 0, "S": 0, "P": 0}
	c = 0
	output = random.choice(["R", "S", "P"])
	counts[output] += 1
	
	hst.append(output)
else:
	c += 1
	hst[c-1] += input
	
	if rwd[hst[c-1]] < 0:
		hst[c-1] = opp[hst[c-1][1]] + hst[c-1][1]
		for r in rwd:
			if rwd[r] < 0:
				rwd[r] -= inc
			elif rwd[r] >= 0:
				rwd[r] += inc
	else:
		if rwd[hst[c-1]] == 0:
			hst[c-1] = opp[hst[c-1][1]] + hst[c-1][1]
		
		for r in rwd:
			if rwd[r] < 0:
				rwd[r] += inc
			elif rwd[r] >= 0:
				rwd[r] -= inc
	
	counts[hst[c-1][0]] += 1
	rec[hst[c-1]].insert(0, c-1)
	if len(rec[hst[c-1]]) > rtr:
		#rec[hst[c-1]].pop(random.randint(0, len(rec[hst[c-1]]) - 1,))
		rec[hst[c-1]].pop(len(rec[hst[c-1]]) - 1)
	
	scores = {"R": inc, "S": inc, "P": inc}
	for option in ("RS", "RP", "SR", "SP", "PR", "PS", "RR", "SS", "PP"):
		me = option[0]
		for i in rec[option]:
			#if option == hst[i]:
			t = len(hst) - i
			k = i - 1
			count = 0
			for j in xrange(i - 1, max(int(i - 1 - wdw/5), -1), -1):
				if hst[k][1] == hst[j][1]:
					count += 1
				
				k =- 1
			
			scores[me] += dsc**t * rwd[option] * float(count)/min(len(hst), wdw)
	
	best_score = 0
	best_choice = random.choice(["R", "S", "P"])
	for opt in ("R", "S", "P"):
		score = scores[opt] * float(counts[opt])/len(hst)
		
		if (score > best_score):
			best_score = score
			best_choice = opt
	
	output = best_choice
	counts[output] += 1
	hst.append(output)