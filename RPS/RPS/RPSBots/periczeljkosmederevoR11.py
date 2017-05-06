import random
r = 0
p = 0
s = 0
o = ""
while o == "":
   o = random.choice(["R","P","S","R","P","S","R","P","S","R","R","R","P","P","P","S","S","S"]) 
   if o == "R":
      if r<34:
         r = r + 1
      else:
         o = ""
   elif o == "P":
      if p < 34:
         p = p + 1
      else: 
         o = ""
   elif o == "S": 
      if s < 34:
         s = s + 1
      else: 
         o = ""
   if ( r > 33 & p > 33 & s > 33 ):
      r = 0
      p = 0
      s = 0
else:
  output = o