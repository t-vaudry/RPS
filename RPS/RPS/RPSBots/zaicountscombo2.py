# this mixes the predictions of the two strategies instead of just switches

# --------------------- initialization -----------------------------
if not input:
   import random
   import math
   import itertools, operator, functools
   
   # constants
   ROUNDS = 1000
   R, P, S = 0, 1, 2
   RPS_NUM = (R, P, S)
   RPS_STR = 'RPS'
   WIN, TIE, LOSE = 1, 0, -1
   
   def to_num(h):
      return RPS_STR.index(h)

   def to_str(i):
      return RPS_STR[i]

   def play(h1, h2):
      return (h1 - h2 + 4) % 3 - 1

   def diff(h1, h2):
      return (h1 - h2 + 3) % 3

   def undiff(h, d):
      return (h + d + 3) % 3

   def beats(h):
      return undiff(h, WIN)

   def loses(h):
      return undiff(h, LOSE)

   def ties(h):
      return undiff(h, TIE)

   def pick_random(lst):
      i = random.randint(0, len(lst) - 1)
      return (i, lst[i])

   def my_max(val1, val2):
      return val1 if val1[1] > val2[1] else val2

   def pick_max(lst):
      return reduce(my_max, enumerate(lst))

   def pick_weighted(lst, sumlst=None):
      r = random.uniform(0.0, sumlst or sum(lst))
      acc = 0.0
      for i, w in enumerate(lst):
         acc += w
         if r <= acc:
            return (i, w)

   def skew(lst):
      m = max(float(max(lst)), 1.0)
      # m = min(lst) / 2.0
      for i, x in enumerate(lst):
         lst[i] = (x / m)
         # lst[i] = x - m
   
   def shift(lst):
      m = min(min(lst), 0)
      return [(x - m) for x in lst]
   
   def random_hand():
      return random.choice(RPS_NUM)
   
   COUNT_ORDER_MAX = 7
   POWERS3 = tuple(3 ** x for x in xrange(COUNT_ORDER_MAX+1))
   
   # little endian ternary number
   def ternary(vec):
      return sum(itertools.imap(operator.mul, vec, POWERS3))

   def emptycounts(n):
      return tuple(tuple([0.0] * 3 for x in RPS_NUM) for i in xrange(n))

   def weigh_match(hands_played):
      return 2 ** (hands_played / 14.0)

   def weigh_order(weight, order):
      return weight * 2 ** (order)
   
   op_counts = tuple(emptycounts(POWERS3[n]) for n in xrange(COUNT_ORDER_MAX+1))
   my_counts = tuple(emptycounts(POWERS3[n]) for n in xrange(COUNT_ORDER_MAX+1))
   
   STRATEGIES = 2
   DECAY = 0.9
   strategy_scores = [0.0] * STRATEGIES
   next_hand_weights = [[0.0] * 3 for x in xrange(STRATEGIES)]
   count_random = 0
   
   my_hands = []
   op_hands = []
   
   output = to_str(random_hand())
   my_hands.append(to_num(output))
   
# --------------------- turn -----------------------------
else:
   op_hands.append(to_num(input))
   
   hands_played = len(my_hands)
   my_last_hand = my_hands[-1]
   op_last_hand = op_hands[-1]
   my_last_score = play(my_last_hand, op_last_hand)
   op_last_score = play(op_last_hand, my_last_hand)
   
   for i in xrange(STRATEGIES):
      # score the strategies
      last_score = 0.0
      for j in RPS_NUM:
         last_score += next_hand_weights[i][j] * play(j, op_last_hand)
      strategy_scores[i] *= DECAY
      strategy_scores[i] += last_score
   
   # update the counts
   for order in xrange(min(hands_played - 1, COUNT_ORDER_MAX) + 1):
      # update counts for my hands
      my_ix = ternary(my_hands[-order-1:-1])
      my_counts[order][my_ix][my_last_score][my_last_hand] += weigh_match(hands_played)
      # update counts for op hands
      op_ix = ternary(op_hands[-order-1:-1])
      op_counts[order][op_ix][op_last_score][op_last_hand] += weigh_match(hands_played)
   
   # use counts to determine the next move
   next_hand_weights = [[0.0] * 3 for x in xrange(STRATEGIES)]
   for order in xrange(min(hands_played, COUNT_ORDER_MAX) + 1):
      # use my and op hands to determine the next move
      my_ix = ternary(my_hands[-order:] if order != 0 else [])
      my_curr_counts = my_counts[order][my_ix]
      op_ix = ternary(op_hands[-order:] if order != 0 else [])
      op_curr_counts = op_counts[order][op_ix]
      for i in RPS_NUM:
         next_hand_weights[0][i] += weigh_order(my_curr_counts[LOSE][beats(i)], order)
         next_hand_weights[1][i] += weigh_order(op_curr_counts[WIN][loses(i)], order)
         # next_hand_weights[2][i] += weigh_order(op_curr_counts[WIN][loses(i)], order) + weigh_order(op_curr_counts[TIE][loses(i)], order) + weigh_order(op_curr_counts[LOSE][loses(i)], order)
         # next_hand_weights[2][i] += weigh_order(my_curr_counts[TIE][loses(i)], order)
         # next_hand_weights[3][i] += weigh_order(op_curr_counts[TIE][loses(i)], order)
         # next_hand_weights[2][i] += weigh_order(my_curr_counts[WIN][ties(i)], order)
         # next_hand_weights[3][i] += weigh_order(op_curr_counts[LOSE][ties(i)], order)
   
   next_hand_weights_total = [0.0] * 3
   for i in xrange(STRATEGIES):
      skew(next_hand_weights[i])
      if strategy_scores[i] < 0:
         for j in RPS_NUM:
            next_hand_weights_total[j] += next_hand_weights[i][beats(j)] * (-strategy_scores[i])
      else:
         for j in RPS_NUM:
            next_hand_weights_total[j] += next_hand_weights[i][ties(j)] * (strategy_scores[i])
   
   # shifted_weights = [max(p, 0) for p in next_hand_weights_total]
   # shifted_weights = shift(next_hand_weights_total)
   shifted_weights = (next_hand_weights_total)
   if sum(shifted_weights) <= 0:
      # count_random += 1
      output = to_str(random_hand())
   else:
      output = to_str(ties(pick_weighted(shifted_weights)[0]))
   # if hands_played % 99 == 0:
      # print(strategy_scores)
   my_hands.append(to_num(output))
   
   # if hands_played == 999:
      # print(count_random)