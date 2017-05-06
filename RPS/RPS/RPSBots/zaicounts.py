# counts the opponents hands and the wins/ties/losses of each hand
# keeps counts of only the last x played hands where x is currently 1000/5=200
# counts the # of times the hand was won and tied to predict the next one

# the value beats the key
beats = {'R':'P', 'P':'S', 'S':'R'}

# returns a weighted random choice of R, P or S
# default with no arguments is uniformly random
def rand_hand(probs=None,sum=None):
   if probs is None:
      return random.choice(['R', 'P', 'S'])
   else:
      if sum is None:
         sum = probs['R'] + probs['P'] + probs['S']
      if sum < 0.5:
         return random.choice(['R', 'P', 'S'])
      r = random.uniform(0, sum)
      if r < probs['R']:
         return 'R'
      elif r < probs['R'] + probs['P']:
         return 'P'
      else:
         return 'S'

def win(mine, other):
   return mine == beats[other]

def play(mine, other):
   if beats[mine] == other:
      return LOSE
   elif mine == other:
      return TIE
   else:
      return WIN

# count the # of hands from i down to i_inf
# organize the counts by if win, tie or lose
def count_hands(i, i_inf, hand):
   counts = [0, 0, 0]
   for j in xrange(i, i_inf - 1, -1):
      if op_hands[j] == hand:
         counts[play(op_hands[j], my_hands[j])] += 1
   return counts

# start
if input == '':
   import random
   
   ROUNDS = 1000
   WIN = 1
   TIE = 0
   LOSE = -1
   
   my_hands = []
   op_hands = []
   hands_played = 1
   counts = {'R':[0,0,0], 'P':[0,0,0], 'S':[0,0,0]}
   count_num = 0
   
   output = rand_hand()
   my_hands.append(output)
else:
   op_hands.append(input)
   
   i = hands_played - 1
   
   counts[op_hands[i]][play(op_hands[i], my_hands[i])] += 1
   count_num += 1
   
   dist_sup = min(hands_played, ROUNDS / 5)
   
   if dist_sup < count_num:
      j = i-dist_sup+1
      counts[op_hands[j]][play(op_hands[j], my_hands[j])] -= 1
      count_num -= 1
   
   predictions = {'R':counts['R'][WIN] + counts['R'][TIE], 'P':counts['P'][WIN] + counts['P'][TIE], 'S':counts['S'][WIN] + counts['S'][TIE]}
   prediction = rand_hand(probs=predictions)
   output = beats[prediction]
   
   my_hands.append(output)
   hands_played += 1