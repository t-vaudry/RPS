# increment a list of differences to change the pattern when tieing or losing

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
   
   def random_hand():
      return random.choice(RPS_NUM)
   
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
   
   ORDER_MAX = 7
   deltas = [0] * ORDER_MAX
   
   def increment(ds, i):
      carry = i
      for i in xrange(len(ds)):
         val = ds[i] + carry
         carry = val / 3
         ds[i] = val % 3
   
   def step(ds):
      for i in xrange(len(ds)-1, 0, -1):
         ds[i-1] = undiff(ds[i-1], ds[i])
   
   lost = False
   offset = random_hand()
   
   my_hands = []
   op_hands = []
   
   counts = [0] * 3
   
   next_hand = offset
   output = to_str(random_hand())
   my_hands.append(next_hand)
   
# --------------------- turn -----------------------------
else:
   op_hands.append(to_num(input))
   
   hands_played = len(my_hands)
   my_last_hand = my_hands[-1]
   op_last_hand = op_hands[-1]
   my_last_score = play(my_last_hand, op_last_hand)
   op_last_score = play(op_last_hand, my_last_hand)
   
   step(deltas)
   counts[my_last_score] += 1
   if my_last_score == LOSE:
      increment(deltas, 2)
   elif my_last_score == TIE:
      increment(deltas, 1)
   
   next_hand = undiff(offset, deltas[0])
   
   output = to_str(next_hand)
   my_hands.append(next_hand)
   
   # if hands_played % 100 == 0:
      # print(deltas)
   
   # if hands_played == 999:
      # print(counts)