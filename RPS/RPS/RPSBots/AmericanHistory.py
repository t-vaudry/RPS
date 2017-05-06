import random
if input == "":
   count=0
   running=0
   lastchoice=""
if running==0:
   running=random.randint(1,5)
   lastchoice=random.choice(["P","S","R"])
   output=lastchoice
elif running > 0 :
   running=running - 1
   output=lastchoice
if running%2 == 0 :
   output=random.choice(["P","S","R"])