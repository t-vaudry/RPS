# somewhat more random

import math
import random

beats = {'R':'P', 'P':'S', 'S':'R'}

def randHand():
   return random.choice(['R', 'P', 'S'])

def prob(p):
   return random.random() < p

def response(mine, other):
   if mine == other:
      return other if prob(0.7) else beats[beats[other]]
   elif beats[mine] == other:
      return beats[other] if prob(0.8) else other
   else:
      return mine if prob(0.7) else beats[beats[mine]]


# start of main code
if input == '':
   ROUNDS = 1000
   whisker_length = 19
   
   my_hands = []
   opp_hands = []
   
   output = randHand()
   my_hands.append(output)
   hands = 1
else:
   opp_hands.append(input)
   
   #if (hands / whisker_length) % 2 == 0:
   if hands < whisker_length:
      output = randHand()
   else:
      index = hands - whisker_length
      output = response(my_hands[index], opp_hands[index])
   
   my_hands.append(output)
   hands += 1