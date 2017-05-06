import random
if input == "":
   output = "P"
   rr = 0
   rp = 0
   rs = 0
   pr = 0
   pp = 0
   ps = 0
   sr = 0
   sp = 0
   ss = 0
   total = 0
   prev = ""
if input == "R":
   if prev == "":
      output = "P"
      pass
   if prev == "R":
      rr += 1
   if prev == "P":
      rp += 1
   if prev == "S":
      rs += 1
   total = rr+rp+rs+0.1
   probr = rr/float(total)
   probs = rs/float(total)
   probp = rp/float(total)
   v = random.random()
   if v < probr:
      output = "P"
   elif v-probr < probs:
      output = "R" 
   else:
      output = "S"
   prev = "R"
if input == "P":
   if prev == "":
      output = "S"
      pass
   if prev == "R":
      pr += 1
   if prev == "P":
      pp += 1
   if prev == "S":
      ps += 1
   total = pr+pp+ps+0.1
   probr = pr/float(total)
   probs = ps/float(total)
   probp = pp/float(total)
   v = random.random()
   if v < probr:
      output = "P"
   elif v-probr < probs:
      output = "R" 
   else:
      output = "S"
   prev = "P"
if input == "S":
   if prev == "":
      output = "R"
      pass
   if prev == "R":
      sr += 1
   if prev == "P":
      sp += 1
   if prev == "S":
      ss += 1
   total = sr+sp+ss+0.1
   probr = sr/float(total)
   probs = ss/float(total)
   probp = sp/float(total)
   v = random.random()
   if v < probr:
      output = "P"
   elif v-probr < probs:
      output = "R" 
   else:
      output = "S"
   prev = "S"