#alysondp_test
import random
history = []
my_history = []
beat={'R':'P','P':'S','S':'R'}
next_move={'R':0,'P':0,'S':0}

if input == "": # initialize variables for the first round
	rockCount = paperCount = scissorsCount = 0
elif input == "R":
	rockCount += 1
elif input == "P":
	paperCount += 1
elif input == "S":
	scissorsCount += 1

if input != "":
    history.insert(0,input)
    print history

if len(history) >= 4:
    x = 3
    match = 0
    while(x>0):
	min_history = history[0:x]
	for i in range(1,len(history)-x):
	    if min_history == history[i:i+x]:
		next_move[history[i-1]] += 1
		match += 1
	if match != 0:
	    x = 0			
	x = x-1
    if next_move['R'] > next_move['P'] and next_move['R'] > next_move['S']:
	output = 'P' # paper beats rock
    elif next_move['P'] > next_move['S']:
	output = 'S' # scissors beats paper
    else:
	output = 'R' # rock beats scissors
else:
    output = random.choice(['R','S','P'])

my_history.insert(0,output)