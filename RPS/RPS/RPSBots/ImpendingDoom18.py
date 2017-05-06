import random, math
CHOICES = ["R","P","S"]
WEIGHTEDCHOICES = ["R","P","S",'P']
HOWFARBACK = 5
HOWFARBACK2 = 5
STARTLEN = 1

A = [-0.467,  1.595, 6.540]
B = [-0.535, -1.983, 1.138]
C = [-1.325,  3.158, 2.303]
EA = [2.16, 1.82, 1.79]
EB = [1.80, 1.42, 1.72]
EC = [1.97, 1.26, 1.51]

#EA = [1,1,1]
#EB = [1,1,1]
#EC = [1,1,1]

def run(input = []):
	global nmehistory
	global myhistory
	global output
	input = input
	if not input:
		nmehistory = []
		myhistory = []
		choice = dumbchoice()
		myhistory.append(choice)
		output = choice
	else:
		nmehistory.append(input)
		choice = worker(nmehistory,myhistory)
		myhistory.append(choice)
		output = choice


def dumbchoice(randmode=False):
	if randmode:
		return random.choice(CHOICES)
	else:
		return random.choice(WEIGHTEDCHOICES)

def strongagainst(choice):
	if choice == "R": return "P"
	if choice == "P": return "S"
	if choice == "S": return "R"

def weakagainst(choice):
	if choice == "R": return "S"
	if choice == "P": return "R"
	if choice == "S": return "P"

def analyze(p1,p2):
	global A
	global B
	global C
	if len(p1) < STARTLEN:
		#start random?
		return dumbchoice()

	p1last = {'R':0,'P':0,'S':0} #p1 last choice
	p1cnt = {'R':0,'P':0,'S':0}  #count of p1 choices
	p1trnd = {'R':0,'P':0,'S':0}  #extra points for recent choices

	#load the last
	p1last[p1[-1]] = 1

	#p1 choices in percents (0->1)
	p1cnttotal = float(len(p1))
	p1cnt['R'] = p1.count("R") / p1cnttotal
	p1cnt['P'] = p1.count("P") / p1cnttotal
	p1cnt['S'] = p1.count("S") / p1cnttotal

	#recent p1 choices
	p1trnd['R'] = p1[-HOWFARBACK:].count("R")
	p1trnd['P'] = p1[-HOWFARBACK:].count("P")
	p1trnd['S'] = p1[-HOWFARBACK:].count("S")

	p2last = {'R':0,'P':0,'S':0} #p2 last choice
	p2cnt = {'R':0,'P':0,'S':0}  #count of p2 choices
	p2trnd = {'R':0,'P':0,'S':0}  #extra points for recent choices

	#load the last
	p2last[p2[-1]] = 1

	#p2 choices in percents (0->1)
	p2cnttotal = float(len(p2))
	p2cnt['R'] = p2.count("R") / p2cnttotal
	p2cnt['P'] = p2.count("P") / p2cnttotal
	p2cnt['S'] = p2.count("S") / p2cnttotal

	#recent p2 choices
	p2trnd['R'] = p2[-HOWFARBACK:].count("R")
	p2trnd['P'] = p2[-HOWFARBACK:].count("P")
	p2trnd['S'] = p2[-HOWFARBACK:].count("S")


	choice = dumbchoice()
	choiceval = 1
	#A=[.5,.5,-1]
	#B=[1,1,-1]
	#C=[1,1,-1]
	for c in CHOICES:
		cs = strongagainst(c)
		cw = weakagainst(c)
		#run an algorithm for r,p, and s
		peram1 = A[0] * p1cnt[c]  ** EA[0] + A[1] * p2cnt[cw]  **EA[1] + A[2] * p2cnt[cs]  ** EA[2]
		peram2 = B[0] * p1trnd[c] ** EB[0] + B[1] * p2trnd[cw] **EB[1] + B[2] * p2trnd[cs] ** EB[2]
		peram3 = C[0] * p1last[c] ** EC[0] + C[1] * p2last[cw] **EC[1] + C[2] * p2last[cs] ** EC[2]
		#print int(peram1),int(peram2),int(peram3),"|",
		tryval =  peram1 + peram2 + peram3
		if tryval > choiceval:
			choiceval = tryval
			choice = c

	return choice

def lookback(p1):

	p1pat = "".join(p1[-HOWFARBACK2:])
	p1hist = "".join(p1[:-HOWFARBACK2])
	p1analysis = p1hist.split(p1pat)[1:]
	if p1analysis:
		counts = {'S':0,'P':0,'R':0}
		num = 0.0
		for s in p1analysis:
			counts[s[0]] += 1
			num += 1
		probable = sorted(counts, key=counts.get)[0]
		return (probable, counts[probable]/num)
	else:
		return (None, 0)




def worker(nme,me):
	nmechoice = strongagainst(analyze(nme,me))
	mychoice = analyze(me,nme)

	#pattern matcher
	h, hc = lookback(nme)
	if hc > .7:
		choice = h

	elif mychoice == nmechoice:
		choice = strongagainst(mychoice)
	else:
		choice = nmechoice
	#print nmechoice, mychoice
	return choice


run()