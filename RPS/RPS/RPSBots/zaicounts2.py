# weighted frequency counting with decay

# numerical representation
def to_num(h):
   return 'RPS'.index(h)

# convert back to string
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

# returns a weighted random choice of R, P or S
# default with no arguments is uniformly random
def rand_hand(pvec=None):
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
   import random
   
   ROUNDS = 1000
   R = 0
   P = 1
   S = 2
   RPS = [R,P,S]
   WIN = 1
   TIE = 0
   LOSE = -1
   
   decay = 0.97
   
   my_hands = []
   op_hands = []
   counts = [[0.0] * 3 for x in RPS]
   
   output = to_str(rand_hand())
   my_hands.append(to_num(output))
else:
   op_hands.append(to_num(input))
   
   i = len(my_hands) - 1
   
   for score in RPS:
      for hand in RPS:
         counts[score][hand] *= decay
   counts[play(op_hands[i], my_hands[i])][op_hands[i]] += 100.0
   
   # dmax = ROUNDS / 10
   # if dmax < len(my_hands):
      # j = i-dmax+1
      # counts[play(op_hands[j], my_hands[j])][op_hands[j]] -= 1
   
   predictions = [counts[WIN][k] + counts[TIE][k]/2 for k in RPS]
   prediction = rand_hand(predictions)
   output = to_str(beats(prediction))
   
   my_hands.append(to_num(output))