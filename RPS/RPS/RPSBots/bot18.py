# https://github.com/miguel-cv 
import random
if input == "":
	output = random.choice(["S","P"])
	lastinput="P"
	lastinput2="S"
	input=output
	countr=3
	countp=1
	counts=5
	temp=0
if input == "R" :
	#output = random.choice(["S","P"])
	countr=countr+2
if input == "P" : 
   #output= random.choice(["P","R"])
   countp=countp+3
if input == "S" : 
   #output=random.choice(["R","S"])
   counts=counts+7
if input=="R" :
  if lastinput2=="P":
    if lastinput=="S":
      output="S"
    elif lastinput2=="R":
	output="R"
    elif lastinput=="S":
      output="S"
lastinput2=lastinput
lastinput=input  
if counts >0:
  if countr % counts > random.choice([1-3]):
    output=random.choice([output,"R","P","S"]);
if countp >0:
  if countr % countp > random.choice([1-3]):
    output=random.choice([output,"R","P","S"]);
if countr > counts:
    lastinput2=input
else:
  lastinput2=output
if countp > countr:
  lastinput="S"
if countr >0:
  if countr % 9 > random.choice([0-9]):
    input="S"
if lastinput2==output:
  if lastinput2=="R":
    output=random.choice(["P","R"]);
  if lastinput2=="S":
    output=random.choice(["S","R"]);
  if lastinput2=="P":
    output=random.choice(["P","S"]);