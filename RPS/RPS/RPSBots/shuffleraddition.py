import random
array = []
if input == "":
   v = random.randint(0,2)
   if v == 0:
      output = "R"
   elif v == 1:
      output = "P"
   else:
      output = "S"
else:
   v = input
   if v == "R":
      array += ["P"]
   elif v == "P":
      array += ["S"]
   else:
      array += ["R"]
   random.shuffle(array)
   output = array[-1]