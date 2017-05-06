import random, math
CHOICES = ["R","P","S"]
HOWFARBACK = 5
STARTLEN = 1

A = [-0.467,  1.595, 6.540]
B = [-0.535, -1.983, 1.138]
C = [-1.325,  3.158, 2.303]
EA = [2.16, 1.82, 1.79]
EB = [1.80, 1.42, 1.72]
EC = [1.97, 1.26, 1.51]


def run(input = []):
	global nmehistory
	global myhistory
	global output
	input = input
	if not input:
		try:
			if not nmehistory:
				nmehistory = []
		except:
			nmehistory = []
		try:
			if not myhistory:
				myhistory = []
		except:
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
		addedchoices = map(strongagainst,nmehistory)
		return random.choice(CHOICES + addedchoices)

def strongagainst(choice):
	if choice == "R": return "P"
	if choice == "P": return "S"
	if choice == "S": return "R"

def weakagainst(choice):
	if choice == "R": return "S"
	if choice == "P": return "R"
	if choice == "S": return "P"

def analyze(p1,p2):
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


	choice = None
	choiceval = 0
	choicetotal = 0.0
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
		choicetotal += abs(tryval)

	return (choice, choiceval/choicetotal)
NE=2
def lookback(p1,distance):

	if len(p1) > 2*distance:
		p1pat = "".join(p1[-distance:])
		p1hist = "".join(p1[:-distance])
		p1analysis = p1hist.split(p1pat)[1:]
		if p1analysis:
			counts = {'S':0,'P':0,'R':0}
			num = 0.0
			for s in p1analysis:
				if s:
					counts[s[0]] += 1
				num += 1
			probable = sorted(counts, key=counts.get,reverse=True)[0]
			return (probable, (counts[probable]/num)**NE)
	return (None, 0)

#DEBUG = False
DEBUG = True
N = [0.3,0.4,0.5,0.5,0.7,0.7,0.5]
cn = [0,0,0,0,0,0,0]
def worker(nme,me):
	nmechoice,nmeconf = analyze(nme,me)
	#mychoice, myconf = analyze(me,nme)

	#pattern matcher
	h, hc = lookback(nme,2)
	h2, h2c = lookback(nme,1)

	if hc > N[0]:
		choice = strongagainst(h)
		cn[0]+= 1
	elif h2c > N[1]:
		choice = strongagainst(h2)
		cn[1]+= 1
	elif nmechoice and nmeconf > N[2]:
		choice = strongagainst(nmechoice)
		cn[2]+= 1
	else:
		cn[3]+= 1
		choice = dumbchoice()
	#print nmechoice, mychoice

	hm, hmc = lookback(me,2)
	hm2, hm2c = lookback(me,1)

	if hmc > N[3] and choice == hm:
		if random.random() > N[4]:
			choice = strongagainst(choice)
	elif hm2c > N[5] and choice == hm2:
		if random.random() > N[6]:
			choice = strongagainst(choice)


	return choice

run()