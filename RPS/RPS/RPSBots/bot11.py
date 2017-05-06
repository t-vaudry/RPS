import random
if input == "":
	output = random.choice(["S","P"])
	lastinput="P"
	lastinput2="S"
	input=output
	countr=0
	countp=0
	counts=0
if input == "R" :
	output = random.choice(["S","P"])
	countr=countr+1
if input == "P" : 
   output= random.choice(["P","R"])
   countp=countp+1
if input == "S" : 
   output=random.choice(["R","S"])
   counts=counts+1
lastinput2=lastinput
lastinput=input
if input=="R" :
  if lastinput2=="P":
    if lastinput=="S":
      output="S"
    elif lastinput2=="R":
	output="R"
    elif lastinput=="S":
      output="S"
if countr==counts+1 :
  output="R"
if countr==countp+1 :
  output="P"
if random.choice(["R","P","S"]) == output:
	output=lastinput2
if random.choice([1,2,3,4,5,6,7,8,9,10,11,12,13]) == 2:
	output="R"
if random.choice([100,102,103,104,105,1006,27,38,49,610,711,612,143]) == 711:
	output="S"
if random.choice([1-10]) == 5:
	output="R"
if random.choice([1-20]) == 13:
	output="P"
if random.choice([1-30]) == 17:
	output="P"
if random.choice([1-13]) == 13:
	output="R"
if countp==countr+1 :
  output="S"
if counts >0:
  if countr % counts > random.choice([1-3]):
    output=random.choice([output,"R","P","S"]);
if countp >0:
  if countr % countp > random.choice([1-3]):
    output=random.choice([output,"R","P","S"]);
if random.choice([0-13]) == 7:
	output=random.choice(random.choice(input,lastinput2,output,output),random.choice(output,lastinput,lastinput2));
if lastinput2==output:
  if lastinput2=="R":
    output=random.choice(["P","R"]);
  if lastinput2=="S":
    output=random.choice(["S","R"]);
  if lastinput2=="P":
    output=random.choice(["P","S"]);