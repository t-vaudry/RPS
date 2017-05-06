from random import choice

if input == "":
   output= choice(["R", "S", "P"])

if output == "P": 
   if input == "S":
      output = choice(["S", "R"]) 
   else:
      output = output

if output == "S":
   if input == "R":
      output = choice(["R", "P"])
   else:
      output = output

if output == "R":
   if input == "P":
      output = choice(["P", "S"])
   else:
      output = output