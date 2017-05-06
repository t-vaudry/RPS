import random
if input == "": # initialize variables for the first round
	lastone = lasttwo = lastthree = "R"
        count = 0
else:
        lastthree=lasttwo
        lasttwo=lastone
        lastone=input

if lastone == lasttwo and lastone == lastthree:
   if lastone == "R":
      output="P"
   elif lastone == "P":
      output="S"
   elif lastone == "S":
      output="R"

if lastone == lasttwo and lastone != lastthree:
   if lastthree == "R":
      output="P"
   elif lastthree == "P":
      output="S"
   elif lastthree == "S":
      output="R"

if lastone != lasttwo and lastone == lastthree:
   if lasttwo == "R":
      output="P"
   elif lasttwo == "P":
      output="S"
   elif lasttwo == "S":
      output="R"
count=count+1
if lastone != lasttwo and lastone != lastthree or count%2 == 0 :
      output = random.choice(["R","P","S"])