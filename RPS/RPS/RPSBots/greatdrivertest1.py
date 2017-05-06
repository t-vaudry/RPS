import random

if input == "": # initialize variables for the first round
	r=p=s=0
elif input == "R":
	r=r+1
elif input == "P":
	p=p+1
elif input == "S":
	s=s+1
if input == "":
    output="S"
else:
  choice = random.randrange(r+p+s)
  if choice < r:
      output="P"
  elif choice < r+p:
      output = "S"
  else:
      output = "R"