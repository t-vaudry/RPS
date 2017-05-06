# greedy history pattern match
# greedy - use highest available order and most recent
# order 6 - should be slightly faster than order 7 but just as good
# use my hands, op hands, as well as both to predict next hands
# update only the orders that are >= the order last used to make the prediction
#   - something from PPM compression
# choose the strategy with the best score
# choose the meta strategy using an additional history matching corrector
#    which matches using past meta choices and the corresponding payoffs
#    even though I use a history matcher, it seems order 1 is the best
# a little bit of decay goes a long way
# this bot is mostly deterministic
# this beats bayes14 and bayes15 approximately 70% - 80% of the time, but it's
#    still not as effective and ties a lot more with other bots

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
	topoints = [0, 1, -1]
	
	encode1hand = [1,2,3]
	decode1hand = [None, R, P, S]
	
	encode2hands = [[1,2,3], [4,5,6], [7,8,9]]
	decode2hands = [None,(R,R),(R,P),(R,S),(P,R),(P,P),(P,S),(S,R),(S,P),(S,S)]
	
	encodemeta = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]
	
	ORDER = 6
	CORRECTOR_ORDER = 1
	power3 = [0] + [3 ** i for i in xrange(ORDER)]
	power9 = [0] + [9 ** i for i in xrange(ORDER)]
	power18 = [0] + [18 ** i for i in xrange(CORRECTOR_ORDER)]
	
	my_history = collections.defaultdict(lambda: None)
	op_history = collections.defaultdict(lambda: None)
	both_history = collections.defaultdict(lambda: None)
	corrector_history = collections.defaultdict(lambda: None)
	corrector_history[0] = [0] * 6
	corrector_predict = corrector_history[0]
	
	my_last_used_order = 0
	op_last_used_order = 0
	both_last_used_order = 0
	corrector_last_used_order = 0
	
	DECAY = 0.94
	STRATEGIES = 18
	
	META_DECAY = 0.94
	META_STRATEGIES = 6
	
	# 0-2 is my my, 3-5 is my op, 6-8 is both op my, 9-11 is op op, 12-14 is both my, 15-17 is both op
	strategy_scores = [0.0] * STRATEGIES
	reverse_strategy_scores = [0.0] * STRATEGIES
	next_hands = [None] * STRATEGIES
	
	next_hands_meta = [None] * META_STRATEGIES
	
	meta_picks = []
	
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
	
	last_payoff = scoreround[my_last_hand][op_last_hand]
	
	my_hands_encoded.append(my_last_hand_encoded)
	op_hands_encoded.append(op_last_hand_encoded)
	both_hands_encoded.append(both_last_hand_encoded)
	
	# decay the scores
	for i in xrange(STRATEGIES):
		strategy_scores[i] *= DECAY
		reverse_strategy_scores[i] *= DECAY
	
	# update the scores of the strategies if played at least 2 hands
	if hands_played > 1:
		for i in xrange(STRATEGIES):
			strategy_scores[i] += topoints[scoreround[next_hands[i]][op_last_hand]]
			reverse_strategy_scores[i] += topoints[scoreround[next_hands[i]][my_last_hand]]
		
		# update the corrector history
		last_meta_pick = encodemeta[last_payoff][pick_meta_strategy]
		meta_picks.append(last_meta_pick)
		
		corrector_update_index = 0
		if corrector_last_used_order == 0:
			for i in xrange(META_STRATEGIES):
				corrector_history[0][i] *= META_DECAY
				corrector_history[0][i] += topoints[scoreround[next_hands_meta[i]][op_last_hand]]
		
		corrector_predict = corrector_history[0]
		
		for order in xrange(1, CORRECTOR_ORDER+1 if hands_played-1 > CORRECTOR_ORDER else hands_played-1):
			corrector_predict_index = corrector_update_index * 18 + last_meta_pick
			corrector_update_index += meta_picks[-order-1] * power18[order]
			
			if order >= corrector_last_used_order:
				if corrector_history[corrector_update_index] is None:
					corrector_history[corrector_update_index] = [0] * 6
				for i in xrange(META_STRATEGIES):
					corrector_history[corrector_update_index][i] *= META_DECAY
					corrector_history[corrector_update_index][i] += topoints[scoreround[next_hands_meta[i]][op_last_hand]]
			
			corrector_try_get = corrector_history[corrector_predict_index]
			
			if corrector_try_get is not None:
				corrector_predict = corrector_try_get
				corrector_last_used_order = order
		
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
	
	# use the strategy with the best score
	max_score = max(strategy_scores)
	max_list = [i for i in xrange(STRATEGIES) if strategy_scores[i] == max_score]
	pick_strategy = rchoice(max_list)
	
	# use the reverse strategy with the best score
	max_reverse_score = max(reverse_strategy_scores)
	max_reverse_list = [i for i in xrange(STRATEGIES) if reverse_strategy_scores[i] == max_reverse_score]
	pick_reverse_strategy = rchoice(max_reverse_list)
	
	# update the meta strategy
	for f in PAYOFFS:
		next_hands_meta[f] = frompayoff[f][next_hands[pick_strategy]]
		next_hands_meta[f+3] = frompayoff[f][next_hands[pick_reverse_strategy]]
	
	max_meta_score = max(corrector_predict)
	max_meta_list = [i for i in xrange(META_STRATEGIES) if corrector_predict[i] == max_meta_score]
	pick_meta_strategy = rchoice(max_meta_list)
	
	# play the next hand
	output = tostr[next_hands_meta[pick_meta_strategy]]