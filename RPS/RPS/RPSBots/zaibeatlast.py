# frequencies

# --------------------- initialization -----------------------------
if not input:
   import random
   
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
   
   my_hands = []
   op_hands = []
   
   next_hand = random_hand()
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
   
   next_hand = beats(op_last_hand)
   output = to_str(next_hand)
   my_hands.append(next_hand)