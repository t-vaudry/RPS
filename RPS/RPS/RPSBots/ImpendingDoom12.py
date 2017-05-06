import random
CHOICES = ["R","P","S"]
WEIGHTEDCHOICES = ["R","P","S",'P','P','P']
HOWFARBACK = -5


def dumbchoice(randmode=False):
	if randmode:
		return random.choice(CHOICES)
	else:
		return random.choice(WEIGHTEDCHOICES)

def strongagainst(choice):
	if choice == "R": return "P"
	if choice == "P": return "S"
	if choice == "S": return "R"

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
	A=1
	B=3
	C=2
	for c in CHOICES:
		#run an algorithm for r,p, and s
		tryval = A*cnt[c]+B*trnd[c] + C*last[c]
		if tryval > choiceval:
			choiceval = tryval
			choice = c

	#find what is strong against their most probable selection
	option = strongagainst(choice)

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
	
	#don't do somethign predictable-ish
	CUTOFF = 70
	if option == mine:
		perc = random.randrange(1,100)
		if perc > CUTOFF:
			return dumbchoice(randmode=True)

	return option


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