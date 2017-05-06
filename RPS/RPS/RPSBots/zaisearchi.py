# searching for a past pattern and uses it to predict my next worst move

import math
import random

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

# finds the max match from i1 and i2 leftward for my_hands
def search(i1, i2, i_inf, len_sup):
   my_len = 0
   while i1 >= i_inf and i2 >= i_inf and my_len < len_sup and my_hands[i1] == my_hands[i2]:
      i1 -= 1
      i2 -= 1
      my_len += 1
   return my_len

# calculates the weight of a pattern match based on length and distance
# the distance is between the matches
def weight(length, dis, dis_sup):
   len_weight = length ** 2
   # dis_weight = 1
   dis_weight = ((dis_sup - dis) / float(dis_sup))
   return len_weight * dis_weight

# calculates the weights of my next move
def weigh_match(i, dis_sup, len_sup):
   i_inf = max(i - dis_sup, 0)
   weights = {'R':0.0, 'P':0.0, 'S':0.0}
   for j in xrange(i - 1, i_inf - 1, -1):
      my_len = search(j, i, i_inf, len_sup)
      dis = i - j
      # count it only if after that pattern was a loss
      if my_len > 0 and not win(my_hands[j+1], op_hands[j+1]):
         w = weight(my_len, dis, dis_sup)
         if w > 0:
            weights[my_hands[j+1]] += w
   return weights

# uses the calculated weights to make a prediction about my worst next hand
def predict(i, dis_sup, len_sup):
   return rand_hand(weigh_match(i, dis_sup, len_sup))

# start of main code
if input == '':
   my_hands = []
   op_hands = []
   
   output = rand_hand()
   my_hands.append(output)
else:
   op_hands.append(input)
   
   dis_sup = 100
   len_sup = 10
   
   prediction = predict(len(my_hands) - 1, dis_sup, len_sup)
   output = rand_hand({beats[prediction]:0.4,beats[beats[prediction]]:0.6,prediction:0})
   
   my_hands.append(output)