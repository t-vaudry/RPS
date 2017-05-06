import random 

def is_draw(move, opp_move):
	if move == opp_move:
		return True
	return False

def is_win(move, opp_move):
	if move == 0 and opp_move == 2:
		return True

	elif move == 2 and opp_move == 0:
		return False 

	elif move > opp_move:
		return True

	else:
		return False

#set globals
if input == '':
	rounds = 0
	wins_using = [0, 0, 0] #[R P S]
	rps_map = {0: "R", 1: "P", 2: "S"}
	int_map = {"R": 0, "P": 1, "S": 2}
	last_move = None
	move_random = False #boolean 
	diff = 0 #difference in wins 
	threshold = 5#for going random

else: #not first move
	last_opp_move = int_map[input]

#go random while your winning 
if diff > threshold:
	rand = True
elif diff < -1*threshold:
	rand = False

#update stats (based on last round)
if last_move:
	if is_draw(last_move, last_opp_move):
		pass

	elif is_win(last_move, last_opp_move):
		wins_using[last_move] += 1
		diff += 1

	else: #loss
		wins_using[last_move] -= 1
		diff -= 1

#compute next move
if move_random:
	move = random.randint(0,2)

else:
	max_wins = max(wins_using)
	max_win_moves = [i for i, w in enumerate(wins_using) if w == max_wins]
	move = random.choice(max_win_moves)

#update vars
last_move = move
rounds += 1
output = rps_map[move]