# greedy history pattern match
# greedy - use highest available order and most recent
# order 7
# use both my and op hands to predict
# switches between the 6 ways of using this

# --------------------- initialization -----------------------------
if not input:
	import random
	import collections
	
	rchoice = random.choice
	randint = random.randint
	
	# global constants and maps
	R, P, S = 0, 1, 2
	RPS = [R, P, S]
	T, W, L = 0, 1, 2
	PAYOFFS = [T, W, L]
	
	tonum = {'R':R, 'P':P, 'S':S}
	tostr = {R:'R', P:'P', S:'S'}
	# tostr = ['R', 'P', 'S']
	
	# scoreround = {R:{R:T, P:L, S:W}, P:{R:W, P:T, S:L}, S:{R:L, P:W, S:T}}
	# frompayoff = {T:{R:R, P:P, S:S}, W:{R:P, P:S, S:R}, L:{R:S, P:R, S:P}}
	scoreround = [[T, L, W], [W, T, L], [L, W, T]]
	frompayoff = [[R, P, S], [P, S, R], [S, R, P]]
	ties, beats, loses = frompayoff[T], frompayoff[W], frompayoff[L]
	
	# more specific variables
	ORDER = 7
	power9 = [0] + [9 ** i for i in xrange(ORDER)]
	history = collections.defaultdict(lambda: None)
	DECAY = 1.0
	op_strategy_scores = [0.0, 0.0, 0.0]
	my_strategy_scores = [0.0, 0.0, 0.0]
	
	topoints = [0, 1, -1]
	
	# bookkeeping
	op_hands = []
	my_hands = []
	both_hands = []
	hands_played = 0
	
	# first hand
	output = tostr[random.choice(RPS)]
# --------------------- turn -----------------------------
else:
	# bookkeeping
	last_op_hand = tonum[input]
	last_my_hand = tonum[output]
	last_both_hand = last_op_hand * 3 + last_my_hand + 1
	
	last_index = hands_played
	hands_played += 1
	
	op_hands.append(last_op_hand)
	my_hands.append(last_my_hand)
	both_hands.append(last_both_hand)
	
	# decay the scores
	op_strategy_scores[T] *= DECAY
	op_strategy_scores[W] *= DECAY
	op_strategy_scores[L] *= DECAY
	my_strategy_scores[T] *= DECAY
	my_strategy_scores[W] *= DECAY
	my_strategy_scores[L] *= DECAY
	
	# update the scores
	if hands_played > 1:
		# use base_prediction
		op_strategy_scores[T] += topoints[scoreround[frompayoff[T][op_predict]][last_op_hand]]
		op_strategy_scores[W] += topoints[scoreround[frompayoff[W][op_predict]][last_op_hand]]
		op_strategy_scores[L] += topoints[scoreround[frompayoff[L][op_predict]][last_op_hand]]
		my_strategy_scores[T] += topoints[scoreround[frompayoff[T][my_predict]][last_op_hand]]
		my_strategy_scores[W] += topoints[scoreround[frompayoff[W][my_predict]][last_op_hand]]
		my_strategy_scores[L] += topoints[scoreround[frompayoff[L][my_predict]][last_op_hand]]
	
	# update the history, order 0 as a special case
	update_index = 0
	history[0] = last_index
	
	next_both_hand_index = history[0]
	# update the higher orders and predict the next hand
	for order in xrange(1, ORDER+1 if hands_played > ORDER else hands_played):
		predict_index = update_index * 9 + last_both_hand
		
		update_index += both_hands[-order-1] * power9[order]
		history[update_index] = last_index
		
		try_get = history[predict_index]
		if try_get is not None:
			next_both_hand_index = try_get
	
	# use the scores to use the best strategy
	my_predict = my_hands[next_both_hand_index]
	op_predict = op_hands[next_both_hand_index]
	
	best_score = max(max(op_strategy_scores), max(my_strategy_scores))
	best_op_strategies = [p for p in PAYOFFS if op_strategy_scores[p] == best_score]
	best_my_strategies = [p for p in PAYOFFS if my_strategy_scores[p] == best_score]
	pick_strategy = randint(0, len(best_op_strategies) + len(best_my_strategies) - 1)
	
	# if hands_played % 300 == 0:
		# print hands_played, op_strategy_scores, my_strategy_scores
	
	# play the next hand
	if pick_strategy < len(best_op_strategies):
		output = tostr[frompayoff[best_op_strategies[pick_strategy]][op_predict]]
	else:
		pick_strategy -= len(best_op_strategies)
		output = tostr[frompayoff[best_my_strategies[pick_strategy]][my_predict]]