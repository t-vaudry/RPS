# Mbuzi-v0.2 by mcg

import random
beat = {'R':'P','P':'S','S':'R'}
rps = "RPS"
histlen = 30

if input == "":
   lastmoves = ""
   rounds = 0
   output = random.choice(rps)
else:
   rounds = rounds + 1
   lastmoves = (lastmoves + input)[-histlen:]
   if rounds < histlen:
      output = random.choice(rps)
   else:
      output = beat[random.choice(lastmoves)]