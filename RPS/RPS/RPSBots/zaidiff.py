# tries to use higher differences to predict op's next move

import random

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

def last_repeats(lst, cutoff):
   repeats = 1
   last = lst[-1]
   for i in xrange(len(lst) - 2, -1, -1):
      if lst[i] == last and repeats < cutoff:
         repeats += 1
      else:
         break
   return repeats

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
   
   # this is a magic number
   # some numbers work well against rfind2 and bayes14
   # however some other numbers, even right next to the ones that work, fail miserably
   # eg. 39 will win against bayes14 i.e. win 30/30 matches
   # however 38 against bayes14 results in only 3/30 wins
   ORDER_MAX = 35
   
   diffs = tuple([] for n in xrange(ORDER_MAX+1))
   # diff_counts = tuple([0.0] * 3 for n in xrange(ORDER_MAX+1))
   
   my_hands = []
   op_hands = []
   
   output = to_str(randix())
   my_hands.append(to_num(output))
else:
   op_hands.append(to_num(input))
   
   hands = len(my_hands)
   
   # update the diffs and counts
   diffs[0].append(op_hands[-1])
   # curr_diff_count = diff_counts[0]
   curr_diffs = diffs[0]
   curr_last_diff = curr_diffs[-1]
   repeats = last_repeats(curr_diffs, 10)
   # curr_diff_count[curr_last_diff] = last_repeats(curr_diffs, 10)
   # curr_diff_count[beats(curr_last_diff)] = 0
   # curr_diff_count[loses(curr_last_diff)] = 0
   
   best_choice = (repeats, 0, curr_last_diff)
   
   for i in xrange(1, min(hands, ORDER_MAX + 1)):
      diffs[i].append(diff(diffs[i-1][-1], diffs[i-1][-2]))
      # curr_diff_count = diff_counts[i]
      curr_diffs = diffs[i]
      curr_last_diff = curr_diffs[-1]
      repeats = last_repeats(curr_diffs, 10)
      # curr_diff_count[curr_last_diff] = last_repeats(curr_diffs, 10)
      # curr_diff_count[beats(curr_last_diff)] = 0
      # curr_diff_count[loses(curr_last_diff)] = 0
      
      best_choice = max(best_choice, (repeats, i, curr_last_diff))
   
      # if hands % 198 == 0:
         # print(i, diffs[i][-1], diff_counts[i])
   
   best_level = best_choice[1]
   move = best_choice[2]
   for i in xrange(best_level - 1, -1, -1):
      move = rotate(diffs[i][-1], move)
   
   # if hands % 198 == 0:
      # print('best', best_level, best_choice)
      # print('move', move)
   
   prediction = move
   
   output = to_str(beats(prediction))
   my_hands.append(to_num(output))