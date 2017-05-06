# https://github.com/miguel-cv 
import random
if input == "":
	output = random.choice(["S","P"])
	lastinput="P"
	lastinput2="S"
	input=output
	countr=0
	countp=0
	counts=0
output=random.choice(["P","S"])
if input == "R" :
	countr=countr+random.choice([1,3])
if input == "P" : 
   countp=countp+random.choice([1,3])
if input == "S" : 
   counts=counts+2
if input=="R" :
  if lastinput2=="R":
    if lastinput=="S":
      output="S"
    elif lastinput2=="R":
	output="R"
    elif lastinput=="S":
      output="S"
lastinput2=lastinput
lastinput=input  
if input==lastinput2:
  if output==lastinput:
    countp=countr
    counts=countp+1
    countr=counts+2
if counts >0:
  if countr % counts > random.choice([1-3]):
    output=random.choice([output,"R","P","S"]);
    countr=countr-1
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
  if countr % 13 > random.choice([0-13]):
    input="R"
if countp >0:
  if counts % countp > 2:
    input="S"
if counts >0:
  if countr % 7 > random.choice([0-7]):
    input="P"