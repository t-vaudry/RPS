# Originally by David Bau.

import random

def best(stats):
  m = max(stats)
  return random.choice([k for k in xrange(3) if stats[k] == m])

if not input:
  study_stats = {}
  for i in xrange(3):
    for j in xrange(3):
      study_stats[(i, j)] = [0] * 3
  last_stats = [0] * 3
else:
  ilast = {'R':0,'P':1,'S':2}[input]
  last_stats[ilast] += 1
  last_stats = study_stats[(olast, ilast)]

olast = (best(last_stats) + 1) % 3
output = {0:'R',1:'P',2:'S'}[olast]