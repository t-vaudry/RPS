# Name: zai_switch_markov1_ml
# Author: zdg
# Email: rpscontest.b73@gishpuppy.com
# the email is disposable in case it gets spammed
# 
# let's try out some bayes inference with 1-st order markov model wrappers on
#    various strategies as the hypotheses
# uses last diff as well as last payoff to transition for the 1-st order
# uses ML i.e. maximum likelihood learning by minimizing the entropy
# also have some ad-hoc decay which helps a lot

# --------------------- initialization -----------------------------
if not input:
	import random, collections, math
	
	# micro-optimizations
	rchoice = random.choice
	log = math.log
	
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
	
	# entropy of a 3 vector - doesn't need to be normalized
	def entropy(vec):
		v1, v2, v3 = vec
		# force coerce to float
		total = v1 + v2 + v3 + 0.0
		# normalize
		p1, p2, p3 = v1 / total, v2 / total, v3 / total
		if total > 0.0:
			return (-((p1 * log(p1)) if v1 > 0.0 else 0.0)
				- ((p2 * log(p2)) if v2 > 0.0 else 0.0)
				- ((p3 * log(p3)) if v3 > 0.0 else 0.0))
		else:
			# entropy of nothing is undefined, but here it's useful to define it
			#    as the same as completely random
			return 1.0
	
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
	# contexts = [[1.0, 1.0, 1.0] for _ in BOTS]
	
	# 1st order transition matrix
	# use both last diff and last payoff for each bot
	markov = [[[1.0 for _ in RPS] for _ in xrange(9)] for _ in BOTS]
	
	# initialize history matching strategies
	my_ghpm = GHPM(6, 3)
	op_ghpm = GHPM(6, 3)
	both_ghpm = GHPM(6, 9)
	
	# first hand is completely random - no reason to do otherwise
	next_hand = seed
	output = tr[next_hand]
	
	bot_diffs = [[] for _ in BOTS]
	bot_payoffs = [[] for _ in BOTS]
	
	# bookkeeping
	hands = 1
	last_ix = 0
	score = 0
# --------------------- turn -----------------------------
else:
	last_my = tr[output]
	last_op = tr[input]
	last_payoff = sub[last_my][last_op]
	
	# keep track of how bots have been playing
	for b in BOTS:
		bot_diffs[b].append(sub[last_op][next_hands[b]])
		bot_payoffs[b].append(sub[last_my][next_hands[b]])
	
	# update the zeroth order markov models
	# for b in BOTS:
		# contexts[b][T] *= DECAY
		# contexts[b][W] *= DECAY
		# contexts[b][L] *= DECAY
		# contexts[b][bot_diffs[b][-1]] += 1.0
	
	# update the first order markov models
	if hands >= 2:
		for b in BOTS:
			last_last_diff, last_diff = bot_diffs[b][-2], bot_diffs[b][-1]
			last_last_payoff = bot_payoffs[b][-2]
			last_last_state = enc2[last_last_diff][last_last_payoff]-1
			
			markov[b][last_last_state][T] *= DECAY
			markov[b][last_last_state][W] *= DECAY
			markov[b][last_last_state][L] *= DECAY
			markov[b][last_last_state][last_diff] += 1.0
	
	# use first order markov to calculate each bot's next state distribution
	next_dist = [None] * NUM_BOTS
	for b in BOTS:
		last_state = enc2[bot_diffs[b][-1]][bot_payoffs[b][-1]]-1
		next_dist[b] = markov[b][last_state]
	
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
	
	# find the most likely bot i.e. one with least entropy
	entropies = [-entropy(next_dist[b]) for b in BOTS]
	most_likely = pick_max(entropies)
	
	pred_next = [None] * 3
	for h in RPS:
		pred_next[add[h][next_hands[most_likely]]] = next_dist[most_likely][h]
	next_hand = expected(pred_next)
	
	output = tr[next_hand]
	
	# bookkeeping
	hands += 1
	last_ix += 1
	score += pts[last_payoff]
	
	# if hands % 100 == 0:
		# print markov
		# print next_dist
		# print