import random


def cal_state(op,my): 
	if (op=="R")and(my=="R"):
		return 1 
	if (op=="R")and(my=="P"):
		return 0 
	if (op=="R")and(my=="S"):
		return 2 
	if (op=="P")and(my=="R"):
		return 2 
	if (op=="P")and(my=="P"):
		return 1 
	if (op=="P")and(my=="S"):
		return 0 
	if (op=="S")and(my=="R"):
		return 0 
	if (op=="S")and(my=="P"):
		return 2 
	if (op=="S")and(my=="S"):
		return 1 

def next_move(state, prob):
	if(prob[state][0]>prob[state][1]):
		if (prob[state][2]>prob[state][1]): 
			return "R"
		else: 
			return "P"
	else: 
		if (prob[state][2]>prob[state][0]):
			return "S"
		else: 
			return "P"


prob = [[470,235,538],[858,800,1765],[2890,3322,2814]]

if input=="":
	state = -1 

choices = ["R", "P", "S"];

if state==-1: 
	op_last_move = input	
	if op_last_move=="":		
		my_next_move = random.choice(choices)		
		output = my_next_move		
	else:		
		my_last_move = my_next_move
		state = cal_state(op_last_move,my_last_move) 
		prob[state][choices.index(op_last_move)] +=1		
		my_next_move = next_move(state, prob)		
		output = my_next_move
elif state>-1: 	
	op_last_move = input	
	my_last_move = my_next_move
	state = cal_state(op_last_move, my_last_move)
	prob[state][choices.index(op_last_move)] +=1	
	my_next_move = next_move(state, prob)	
	output = my_next_move