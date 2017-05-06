#alysondp_test
import random

beat={'R':'P','P':'R','S':'P'}
next_move={'R':0,'P':0,'S':0}

if input == "": # initialize variables for the first round
    history = []
    #my_history = []

if input != "":
    history.insert(0,input)
    
if len(history) > 4:
    x = 4
    if len(history) > 100:
        history = history[0:99]
    while(x>0):
	min_history = history[0:x]
	next_move['R'] = next_move['P'] = next_move['S'] = 0
	for i in range(1,len(history)-x):
	    if min_history == history[i:i+x]:
		next_move[history[i-1]] += 1			
	x = x-1
	
    if next_move['R'] > next_move['P'] and next_move['R'] > next_move['S']:
	output = 'P' # paper beats rock
    elif next_move['P'] > next_move['S']:
	output = 'S' # scissors beats paper
    else:
	output = 'R' # rock beats scissors
else:
    output = random.choice(['R','S','P'])

#my_history.insert(0,output)