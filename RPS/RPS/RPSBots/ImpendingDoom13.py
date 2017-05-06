import random
CHOICES = ["R","P","S"]
WEIGHTEDCHOICES = ["R","P","S",'S','S','P']
HOWFARBACK = -3


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

def analyze(nme,me):
	if len(nme) < 3:
		#start random?
		return dumbchoice()
	last = {'R':0,'P':0,'S':0} #enemies last choice
	cnt = {'R':0,'P':0,'S':0}  #count of enemy choices
	trnd = {'R':0,'P':0,'S':0}  #extra points for recent choices

	#load the last
	last[nme[-1]] = 1

	#enemy choices in percents (0->1)
	cnttotal = float(len(nme))
	cnt['R'] = nme.count("R") / cnttotal
	cnt['P'] = nme.count("P") / cnttotal
	cnt['S'] = nme.count("S") / cnttotal

	#recent enemy choices
	trnd['R'] = nme[HOWFARBACK:].count("R")
	trnd['P'] = nme[HOWFARBACK:].count("P")
	trnd['S'] = nme[HOWFARBACK:].count("S")

	choice = dumbchoice()
	choicevalue = 1
	A=2
	B=1
	C=1
	for c in CHOICES:
		#run an algorithm for r,p, and s
		tryval = A*cnt[c]+B*trnd[c] + C*last[c]
		if tryval > choiceval:
			choiceval = tryval
			choice = c

	#find what is strong against their most probable selection
	option1 = strongagainst(choice)

	mine = dumbchoice()
	myvalue = 1
	myr = me.count("R")
	myp = me.count("P")
	mys = me.count("S")
	if myr > myvalue:
		mine = 'R'
	if mys > myvalue:
		mine = 'S'
	if myp > myvalue:
		mine = 'P'

	mapping = zip(me[:-1],nme[1:])
	#see how often they play my weakness the next round
	yes = 1
	no = 1
	for a in mapping:
		if strongagainst(a[0]) == a[1]:
			yes += 1
		else:
			no += 1
	if yes > no:
		#more often than not, they play my weakness, so turn the tables on them
		return weakagainst(me[-1])
	
	#don't do somethign predictable-ish
	CUTOFF = 80
	if option1 == mine:
		perc = random.randrange(1,100)
		if perc > CUTOFF:
			return dumbchoice(randmode=True)


	return option1


input = []

if not input:
	nmehistory = []
	myhistory = []
	choice = dumbchoice()
	myhistory.append(choice)
	output = choice
else:
	nmehistory.append(input)
	choice = analyze(nmehistory,myhistory)
	myhistory.append(choice)
	output = choice