import random

if input == "": # initialize variables for the first round
    count = 0 
    irreq = 1
    output = random.choice(["R","P","S"])
elif input == "R":
	output = "P"
elif input == "P":
	output = "S"
elif input == "S":
	output = "R"

count += 1

if count % irreq == 0 :
   rdm = random.choice(["R","P","S"])

   if rdm == "R": 
      output = "S" 
      irreq = 2
   elif rdm == "P": 
      output = "R" 
      irreq = 4
   elif rdm == "S": 
      output = "P" 
      irreq = 3