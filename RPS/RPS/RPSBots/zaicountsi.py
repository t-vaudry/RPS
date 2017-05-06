# weighted higher order frequency counting with decay
# based on zai_counts3 but counts my worst hands instead of opp best hands
# like a faster version of zai_search_i

import random
from itertools import count, cycle, repeat
from operator import add, mul
from functools import partial

def to_num(h):
   return 'RPS'.index(h)

def to_str(i):
   return 'RPS'[i]

def play(h1, h2):
   return (h1 - h2 + 4) % 3 - 1

def beats(h):
   return (h + 1) % 3

def loses(h):
   return (h + 2) % 3

def ties(h):
   return h

def randix(pvec=None):
   if pvec is None:
      return random.randint(0,2)
   r = random.uniform(0.0, sum(pvec))
   acc = 0.0
   for (i,p) in enumerate(pvec):
      acc += p
      if r <= acc:
         return i
   return random.randint(0,2)

def normalize(vec):
   m = min(vec) / 2
   # m = max(min(vec) - 1, 0)
   for i, x in enumerate(vec):
      vec[i] = x - m

# little endian ternary number
def ternary(vec):
   num = 0
   power = 0
   for i, x in enumerate(vec):
      num += x * POWERS3[i]
   return num

def emptycounts(n):
   return tuple(tuple([0.0] * 3 for x in RPS) for i in xrange(n))

# start
if input == '':
   ROUNDS = 1000
   R = 0
   P = 1
   S = 2
   RPS = [R,P,S]
   WIN = 1
   TIE = 0
   LOSE = -1
   
   ORDER_MAX = 7
   POWERS3 = tuple(3 ** x for x in xrange(ORDER_MAX+1))
   
   order = tuple(emptycounts(POWERS3[n]) for n in xrange(ORDER_MAX+1))
   
   predictions = [0] * (ORDER_MAX + 1)
   
   my_hands = []
   op_hands = []
   
   output = to_str(randix())
   my_hands.append(to_num(output))
else:
   op_hands.append(to_num(input))
   
   hands = len(my_hands)
   
   # update the counts
   
   order_update_max = min(hands-1, ORDER_MAX)
   
   for i in xrange(order_update_max + 1):
      # don't include the last hand
      index = ternary(my_hands[-i-1:-1])
      order[i][index][play(my_hands[-1],op_hands[-1])][my_hands[-1]] += hands * 5
   
   # use counts to make prediction about my next worst hand
   
   order_predict_max = min(hands, ORDER_MAX)
   
   pvec = [0.0, 0.0, 0.0]
   for i in xrange(order_predict_max, -1, -1):
      index = ternary(my_hands[-i:] if i != 0 else [])
      curr_order = order[i][index]
      curr_pvec = [curr_order[LOSE][k] + curr_order[TIE][k] for k in RPS]
      if sum(curr_pvec) > 0:
         pvec[0] += curr_pvec[0] * (i+1)
         pvec[1] += curr_pvec[1] * (i+1)
         pvec[2] += curr_pvec[2] * (i+1)
   normalize(pvec)
   prediction = randix(pvec)
   
   pvec = [0.0, 0.0, 0.0]
   pvec[loses(prediction)] = 0.5
   pvec[beats(prediction)] = 0.5
   output = to_str(randix(pvec))
   # output = to_str(loses(prediction))
   my_hands.append(to_num(output))