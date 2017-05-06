# searching for a past pattern and uses it to predict my next worst move
# some refactoring and different prediction calculation

import math
import random

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
      pvec = [1.0/3.0] * 3
   r = random.uniform(0.0, sum(pvec))
   acc = 0.0
   for (i,p) in enumerate(pvec):
      acc += p
      if r <= acc:
         return i

# finds the max match from i1 and i2 leftward for lst
def search(lst, i1, i2, imin, smax):
   s = 0
   while i1 >= imin and i2 >= imin and s < smax and lst[i1] == lst[i2]:
      i1 -= 1
      i2 -= 1
      s += 1
   return s

# calculates the weight of a pattern match based on length and distance
# the distance is between the matches
def weight(s, d, dmax):
   sw = s ** 2
   # dw = 1
   dw = ((dmax - d) / float(dmax))
   return sw * dw

# calculates the weights of my next move
def weigh_matches(lst, i, dmax, smax):
   imin = max(i - dmax, 0)
   ws = [[0.0] * 3 for x in xrange(3)]
   for j in xrange(i - 1, imin - 1, -1):
      s = search(lst, j, i, imin, smax)
      d = i - j
      ws[play(myhands[j+1], ophands[j+1])][myhands[j+1]] += weight(s, d, dmax)
   return ws

# uses the calculated weights to make a prediction about my worst next hand
def predict(lst, i, dmax, smax):
   ws = weigh_matches(lst, i, dmax, smax)
   return rand_hand([ws[LOSE][j] + ws[TIE][j] / 2 + ws[WIN][j] / 4 for j in xrange(3)])

# start of main code
if input == '':
   ROUNDS = 1000
   R = 0
   P = 1
   S = 2
   WIN = 1
   TIE = 0
   LOSE = -1
   
   myhands = []
   ophands = []
   
   output = to_str(rand_hand())
   myhands.append(to_num(output))
else:
   ophands.append(to_num(input))
   
   dmax = 100
   smax = 10
   
   prediction = predict(myhands, len(myhands) - 1, dmax, smax)
   pvec = [0.0] * 3
   pvec[loses(prediction)] = 0.6
   pvec[beats(prediction)] = 0.4
   output = to_str(rand_hand(pvec))
   
   myhands.append(to_num(output))