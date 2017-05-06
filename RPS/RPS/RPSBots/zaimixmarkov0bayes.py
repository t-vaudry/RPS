# Name: zai_mix_markov0_bayes
# Author: zdg
# Email: rpscontest.b73@gishpuppy.com
# the email is disposable in case it gets spammed
# 
# let's try out some bayes inference with 0-th order markov models as the hypotheses
# seems like some adhoc decay is needed for this to be really effective

# --------------------- initialization -----------------------------
if not input:
	import random, collections, math
	
	# micro-optimizations
	rchoice = random.choice
	
	# global constants and maps
	# using lists and dictionaries because function call and arithmetic is slow
	R, P, S = 0, 1, 2
	RPS = [R, P, S]
	T, W, L = R, P, S
	PAYOFFS = RPS
	tr = {'R':R, 'P':P, 'S':S, R:'R', P:'P', S:'S'}
	sub = [[T, L, W], [W, T, L], [L, W, T]]
	add = [[R, P, S], [P, S, R], [S, R, P]]
	ties, beats, loses = add[T], add[W], add[L]
	
	pts = [0, 1, -1]
	near = [1, 0, 0]
	
	enc1 = [1,2,3]
	dec1 = [None, R, P, S]
	
	enc2 = [[1,2,3], [4,5,6], [7,8,9]]
	dec2 = [None,(R,R),(R,P),(R,S),(P,R),(P,P),(P,S),(S,R),(S,P),(S,S)]
	
	seed = rchoice(RPS)
	
	def pick_max(vec):
		max_val = max(vec)
		max_list = [i for i in xrange(len(vec)) if vec[i] == max_val]
		return rchoice(max_list)
	
	# calculate the hand with the best expected value against the given op hand
	# random only in case of ties
	def expected(vec):
		expected_payoffs = [vec[S] - vec[P], vec[R] - vec[S], vec[P] - vec[R]]
		max_expected = max(expected_payoffs)
		max_list = [i for i in RPS if expected_payoffs[i] == max_expected]
		return rchoice(max_list)
	
	def normalize(vec):
		factor = 1.0 / sum(vec)
		for i in xrange(len(vec)):
			vec[i] *= factor
	
	# greedy history pattern matcher
	# ORDER is the largest context size
	# BASE is the base of the numerical encoding
	# encodes sequences of numbers from 1...BASE as a BASE-adic number
	# encodes the empty sequence as 0
	# apparently this encoding is called a bijective base-BASE system on wikipedia
	class GHPM:
		def __init__(self, ORDER, BASE):
			self.ORDER = ORDER
			self.BASE = BASE
			self.powers = [0] + [BASE ** i for i in xrange(ORDER)]
			self.hist = []
			self.contexts = collections.defaultdict(lambda: None)
			self.pred = None
			self.preds = [None] * (ORDER+1)
		
		def update(self, next_val, up_fun):
			self.hist.append(next_val)
			# update the history, order 0 as a special case
			up_ix = 0
			self.contexts[0] = up_fun(self.contexts[0])
			
			# start the prediction with the zeroth order
			self.pred = self.contexts[0]
			
			# update the higher orders and prediction
			elems = len(self.hist)
			for order in xrange(1, self.ORDER+1 if elems > self.ORDER else elems):
				pred_ix = up_ix * self.BASE + next_val
				
				up_ix += self.hist[-order-1] * self.powers[order]
				self.contexts[up_ix] = up_fun(self.contexts[up_ix])
				
				try_get = self.contexts[pred_ix]
				self.preds[order] = try_get
				if try_get is not None:
					self.pred = try_get
	
	NUM_BOTS = 9
	BOTS = range(NUM_BOTS)
	DECAY = 0.98
	next_hands = [seed for _ in BOTS]
	# contexts = [[0.0, 0.0, 0.0] for _ in BOTS]
	contexts = [[1.0, 1.0, 1.0] for _ in BOTS]
	
	# initialize history matching strategies
	my_ghpm = GHPM(6, 3)
	op_ghpm = GHPM(6, 3)
	both_ghpm = GHPM(6, 9)
	
	# first hand is completely random - no reason to do otherwise
	next_hand = seed
	output = tr[next_hand]
	
	# bookkeeping
	hands = 1
	last_ix = 0
	score = 0
# --------------------- turn -----------------------------
else:
	last_my = tr[output]
	last_op = tr[input]
	last_payoff = sub[last_my][last_op]
	
	# update the contexts for the markov models
	for b in BOTS:
		contexts[b][R] *= DECAY
		contexts[b][P] *= DECAY
		contexts[b][S] *= DECAY
		contexts[b][sub[last_op][next_hands[b]]] += 1.0
	
	# update the history matchers
	my_ghpm.update(enc1[last_my], lambda _:last_ix)
	op_ghpm.update(enc1[last_op], lambda _:last_ix)
	both_ghpm.update(enc2[last_op][last_my], lambda _:last_ix)
	
	# update predictions
	next_hands[1] = last_op
	next_hands[2] = last_my
	
	# hpm
	both_hist = both_ghpm.hist
	# my hist
	pred_op, pred_my = dec2[both_hist[my_ghpm.pred]]
	next_hands[3] = pred_op
	next_hands[4] = pred_my
	# op hist
	pred_op, pred_my = dec2[both_hist[op_ghpm.pred]]
	next_hands[5] = pred_op
	next_hands[6] = pred_my
	# both hist
	pred_op, pred_my = dec2[both_hist[both_ghpm.pred]]
	next_hands[7] = pred_op
	next_hands[8] = pred_my
	
	
	# calculate likelihood of the bots
	likelihoods = [None] * NUM_BOTS
	for b in BOTS:
		cur_context = contexts[b]
		likelihoods[b] = (cur_context[R] ** cur_context[R]) * (cur_context[P] ** cur_context[P]) * (cur_context[S] ** cur_context[S])
	normalize(likelihoods)
	
	# mix together the bots weighted by likelihood
	next_op_dist = [0.0, 0.0, 0.0]
	for b in BOTS:
		for h in RPS:
			next_op_dist[add[h][next_hands[b]]] += likelihoods[b] * contexts[b][h]
	normalize(next_op_dist)
	
	# next_hand = beats[next_hands[pick_max(likelihoods)]]
	next_hand = expected(next_op_dist)
	
	output = tr[next_hand]
	
	# bookkeeping
	hands += 1
	last_ix += 1
	score += pts[last_payoff]
	
	# if hands % 100 == 0:
		# print contexts
		# print likelihoods
		# print next_op_dist, next_hand
		# print