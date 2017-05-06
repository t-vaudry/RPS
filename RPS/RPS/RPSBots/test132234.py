import random

def list_power(base, power_list):
	return [ base**x for x in power_list ]
	
def weighted_choice(choices):
   total = sum(w for c, w in choices)
   r = random.uniform(0, total)
   upto = 0
   for c, w in choices:
      if upto + w >= r:
         return c
      upto += w
   assert False, "Shouldn't get here"


if input == "":
	remember = 7
	currentSeq = [None] * remember
	seqHistR = seqHistP = seqHistS = [0] * sum(list_power(3, [x + 1 for x in range(remember)]))
	strwgts = [x + 1 for x in range(remember)]
	priorwgt = 1
	output = random.choice(["R","P","S"])
else:
	if input == "R":
		n = 0
	if input == "P":
		n = 1
	if input == "S":
		n = 2
	updateidx = currentSeq[:]
	for idx, val in enumerate(updateidx):
		if val is not None:
			updateidx[idx] = updateidx[idx] + pow(3, idx)
	updateidx = [x for x in updateidx if x is not None]
	if len(updateidx) > 0:
		if input == "R":
			for x in updateidx:
				seqHistR[x] = seqHistR[x] + 1 
		if input == "P":
			for x in updateidx:
				seqHistP[x] = seqHistP[x] + 1 
		if input == "S":
			for x in updateidx:
				seqHistS[x] = seqHistS[x] + 1 
	del currentSeq[-1]
	currentSeq = [0] + currentSeq
	for idx, val in enumerate(currentSeq):
		if val is not None:
			currentSeq[idx] = val + n * pow(3, idx)
	currentidx = currentSeq[:]
	for idx, val in enumerate(currentidx):
		if val is not None:
			currentidx[idx] = val + pow(3, idx)
	rock = paper = scissors = priorwgt
	for idx, val in enumerate(currentidx):
		if val is not None:
			rock = rock + seqHistR[val] * strwgts[idx]
			paper = paper + seqHistP[val] * strwgts[idx]
			scissors = scissors + seqHistS[val] * strwgts[idx]
	choices = [["R",rock],["P",paper],["S",scissors]]
	output = weighted_choice(choices)