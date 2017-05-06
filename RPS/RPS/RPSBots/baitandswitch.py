import random
change = { "RR": 0, "RP": -1, "RS": 1, "PR": 1, "PP": 0, "PS": -1, "SR": -1, "SP": 1, "SS": 0 }

if input == "":
   played = 0
   delta = 0
else:
   delta += change[last + input]

if delta < 10:
   if played < 200:
       output = "S"
   else:
       output = "P"
else:
   output = random.choice(["R", "P", "S"])

played += 1
last = output