# Mbuzi-v0.3 by mcg

import random
import math

beat = {'R':'P','P':'S','S':'R'}
rps = "RPS"
histlen = 32
patlen = 3
matchcnt = 12

#chi-square simple randomness check
def randomness(rpsseq):
   n = len(rpsseq)
   r = len(rps)
   nr = n / r;
   chisq = 0.0
   freqs = {}
   for x in rpsseq:
      if x in freqs:
         freqs[x] += 1
      else:
         freqs[x] = 1
   for f in freqs.itervalues():
      tmp = f - nr
      chisq += tmp * tmp
   chisq /= nr
   return abs(chisq - r) / math.sqrt(r)

if input == "":
   lastmoves = ""
   pattern = ""
   opphist = {}
   rounds = 0
else:
   lastmoves = (lastmoves + input)[-histlen:]
   if len(pattern) == patlen:
      opphist[pattern] = opphist.get(pattern, "") + input
   pattern = (pattern + input)[-patlen:]

if rounds < histlen:
   output = random.choice(rps)
elif pattern in opphist and len(opphist[pattern]) >= matchcnt:
   output = beat[random.choice(opphist[pattern])]
elif randomness(lastmoves) < 1.0:
   output = random.choice(rps)
else:
   output = beat[random.choice(lastmoves[histlen/2:])]
rounds += 1