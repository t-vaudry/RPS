import random
import math
import operator
from collections import deque

if input == "":
  oppdeque = deque()
  played = {'R': 0, 'P':0, 'S':0}
  dequesize = 16
  counter = { ('R',): 'P', 
              ('P',): 'S',
              ('S',): 'R',
              ('R','P'): 'P', 
              ('R','S'): 'R',       
              ('P','S'): 'S',
              ('R', 'P', 'S'): None}
  output = random.choice(['R', 'P', 'S']) 
else:
  oppdeque.append(input)
  played[input] += 1
  if len(oppdeque) > dequesize:
    t = oppdeque.popleft()
    played[t] -= 1
  
  m = max(played.values())
  oppbesthandslist = [e[0] for e in played.iteritems() if e[1] == m]
  oppbesthandslist.sort(key=lambda x: {'R':'a', 'P': 'b', 'S': 'c'}[x])
  oppbesthands = tuple(oppbesthandslist)
  output = counter[oppbesthands]
  if output is None:
    output = random.choice(['R','P','S'])