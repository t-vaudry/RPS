# greedy history pattern match
# greedy - use highest available order and most recent
# order 7
# use my hands, op hands, as well as both to predict next op hand
# switch using a fsa between all 6+6+6 = 18 ways of doing it
# update only the orders that are >= the order last used to make the prediction
#   - something from PPM compression

# --------------------- initialization -----------------------------
if not input:
	import random, collections
	
	# micro-optimizations
	rchoice = random.choice
	randint = random.randint
	uniform = random.uniform
	
	# global constants and maps
	R, P, S = 0, 1, 2
	RPS = [R, P, S]
	T, W, L = 0, 1, 2
	PAYOFFS = [T, W, L]
	
	tonum = {'R':R, 'P':P, 'S':S}
	tostr = {R:'R', P:'P', S:'S'}
	
	scoreround = [[T, L, W], [W, T, L], [L, W, T]]
	frompayoff = [[R, P, S], [P, S, R], [S, R, P]]
	ties, beats, loses = frompayoff[T], frompayoff[W], frompayoff[L]
	
	# more specific variables
	topoints = [0.0, 1.0, -1.0]
	
	encode1hand = [1,2,3]
	decode1hand = [None, R, P, S]
	
	encode2hands = [[1,2,3], [4,5,6], [7,8,9]]
	decode2hands = [None,(R,R),(R,P),(R,S),(P,R),(P,P),(P,S),(S,R),(S,P),(S,S)]
	
	ORDER = 7
	power3 = [0] + [3 ** i for i in xrange(ORDER)]
	power9 = [0] + [9 ** i for i in xrange(ORDER)]
	
	my_history = collections.defaultdict(lambda: None)
	op_history = collections.defaultdict(lambda: None)
	both_history = collections.defaultdict(lambda: None)
	
	my_last_used_order = 0
	op_last_used_order = 0
	both_last_used_order = 0
	
	# DECAY = 1.0 # no decay seems to be better
	STRATEGIES = 18
	# 0-2 is my my, 3-5 is my op, 6-8 is both op my, 9-11 is op op, 12-14 is both my, 15-17 is both op
	next_hands = [None for _ in xrange(STRATEGIES)]
	transitions = [[0] * STRATEGIES for _ in xrange(STRATEGIES)]
	
	next_state = randint(0, STRATEGIES-1)
	
	# bookkeeping
	my_hands_encoded = []
	op_hands_encoded = []
	both_hands_encoded = []
	hands_played = 0
	
	# first hand
	output = tostr[rchoice(RPS)]
# --------------------- turn -----------------------------
else:
	# bookkeeping
	last_hand_index = hands_played
	hands_played += 1
	
	my_last_hand = tonum[output]
	my_last_hand_encoded = encode1hand[my_last_hand]
	
	op_last_hand = tonum[input]
	op_last_hand_encoded = encode1hand[op_last_hand]
	
	both_last_hand_encoded = encode2hands[my_last_hand][op_last_hand]
	
	my_hands_encoded.append(my_last_hand_encoded)
	op_hands_encoded.append(op_last_hand_encoded)
	both_hands_encoded.append(both_last_hand_encoded)
	
	# update the transitions if played at least 2 hands
	if hands_played > 1:
		last_transition = transitions[last_state]
		for i in xrange(STRATEGIES):
			# last_transition[i] *= DECAY
			last_transition[i] += topoints[scoreround[next_hands[i]][op_last_hand]]
			if last_transition[i] < 0.0:
				last_transition[i] = 0.0
	
	# update the history, order 0 as a special case
	my_update_index = 0
	op_update_index = 0
	both_update_index = 0
	if my_last_used_order == 0:
		my_history[0] = last_hand_index
	if op_last_used_order == 0:
		op_history[0] = last_hand_index
	if both_last_used_order == 0:
		both_history[0] = last_hand_index
	
	# start the prediction with the zeroth order
	my_predict = my_history[0]
	op_predict = op_history[0]
	both_predict = both_history[0]
	
	# update the higher orders and predict the next hand
	for order in xrange(1, ORDER+1 if hands_played > ORDER else hands_played):
		my_predict_index = my_update_index * 3 + my_last_hand_encoded
		op_predict_index = op_update_index * 3 + op_last_hand_encoded
		both_predict_index = both_update_index * 9 + both_last_hand_encoded
		
		my_update_index += my_hands_encoded[-order-1] * power3[order]
		op_update_index += op_hands_encoded[-order-1] * power3[order]
		both_update_index += both_hands_encoded[-order-1] * power9[order]
		
		if order >= my_last_used_order:
			my_history[my_update_index] = last_hand_index
		if order >= op_last_used_order:
			op_history[op_update_index] = last_hand_index
		if order >= both_last_used_order:
			both_history[both_update_index] = last_hand_index
		
		my_try_get = my_history[my_predict_index]
		op_try_get = op_history[op_predict_index]
		both_try_get = both_history[both_predict_index]
		
		if my_try_get is not None:
			my_predict = my_try_get
			my_last_used_order = order
		if op_try_get is not None:
			op_predict = op_try_get
			op_last_used_order = order
		if both_try_get is not None:
			both_predict = both_try_get
			both_last_used_order = order
	
	my_base_prediction = decode2hands[both_hands_encoded[my_predict]]
	op_base_prediction = decode2hands[both_hands_encoded[op_predict]]
	both_base_prediction = decode2hands[both_hands_encoded[both_predict]]
	
	# update each strategy's prediction
	for f in PAYOFFS:
		next_hands[f] = frompayoff[f][my_base_prediction[0]]
		next_hands[f+3] = frompayoff[f][my_base_prediction[1]]
		next_hands[f+6] = frompayoff[f][op_base_prediction[0]]
		next_hands[f+9] = frompayoff[f][op_base_prediction[1]]
		next_hands[f+12] = frompayoff[f][both_base_prediction[0]]
		next_hands[f+15] = frompayoff[f][both_base_prediction[1]]
	
	# pick the next state
	last_payoff = scoreround[my_last_hand][op_last_hand]
	last_state = next_state
	
	current_transition = transitions[last_state]
	next_state = randint(0, STRATEGIES-1)
	
	total = sum(current_transition)
	u = uniform(0.0, total)
	acc = 0.0
	for i in xrange(STRATEGIES):
		acc += current_transition[i]
		if u < acc:
			next_state = i
			break
	
	# play the next hand
	output = tostr[next_hands[next_state]]