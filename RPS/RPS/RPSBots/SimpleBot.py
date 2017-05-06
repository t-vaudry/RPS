import random
if input == "":
 lastchoice = " "
 lastlastchoice = " "
 output = random.choice(["R","P","S"])
else:
 lastlastchoice = lastchoice
 lastchoice = input
 if lastlastchoice == " ":
  output = random.choice(["R","P","S"])
 else:
  output = lastlastchoice