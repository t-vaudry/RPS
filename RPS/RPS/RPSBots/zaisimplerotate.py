# just cycles through the hands R,P,S and mixes it up sometimes

import random
from itertools import cycle
from operator import mul

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

def diff(h1, h2):
   return (h1 - h2 + 3) % 3

def rotate(h, r):
   return (h + r + 3) % 3

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
   
   score = 0
   score_len = 0
   
   my_hands = []
   op_hands = []
   
   output = to_str(randix())
   my_hands.append(to_num(output))
else:
   op_hands.append(to_num(input))
   
   score += play(my_hands[-1], op_hands[-1])
   score_len += 1
   
   if score_len >= random.randint(3,5) and score < 0:
      output = to_str(my_hands[-1])
      score = 0
      score_len = 0
   else:
      output = to_str(beats(my_hands[-1]))
   
   my_hands.append(to_num(output))