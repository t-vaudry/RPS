#!/usr/bin/env python
import random
import string
def score(input,output):
	if(input=='R' and output =='S' or input=='S' and output =='P' or input=='P' and output =='R'):
		return -1
	if(input=='R' and output =='P' or input=='S' and output =='R' or input=='P' and output =='S'):
		return 1
	return 0
if input == "": # initialize variables for the first round
	rivalHistory=""
	selfHistory=""
	output=random.choice(["R","P","S"])
	selfHistory=output
	solutions=['','','','','','','','','',''];
	scores=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
else:
	for i in range(0,9):
		if(solutions[i]!=''):
			#scores[i]*0.8;
			bonus=score(input,solutions[i]);
			if(bonus*scores[i]<0):
				bonus*=3;
			scores[i]+=bonus;
	rivalHistory=input+rivalHistory
	
	#Solution 0 - Predict Rival
	solutions[0]='';
	len=8
	index=-1
	while(index==-1 and len>0):
		index=rivalHistory.find(rivalHistory[0:len-1],1);
		len-=1;
	if(len!=0):
		expetctedR=rivalHistory[index-1]
		if expetctedR=='R':
			solutions[0]= "P" # paper beats rock
		elif expetctedR=='P':
			solutions[0] = "S" # scissors beats paper
		else:
			solutions[0] = "R" # rock beats scissors
			
	#Solution 1 - Predict self
	solutions[1]='';
	len=8
	index=-1
	while(index==-1 and len>0):
		index=selfHistory.find(selfHistory[0:len-1],1);
		len-=1;
	if(len!=0):
		expetctedS=selfHistory[index-1]
		if expetctedS=='R':
			solutions[1] = "S"
		elif expetctedS=='P':
			solutions[1] = "R"
		else:
			solutions[1] = "P"
			
	#Solution 2 - Random
	solutions[2]=random.choice(["R","P","S"]);
	
	#Solution 3 - Predict Rival, tie
	solutions[3]='';
	len=8
	index=-1
	while(index==-1 and len>0):
		index=rivalHistory.find(rivalHistory[0:len-1],1);
		len-=1;
	if(len!=0):
		solutions[3]=rivalHistory[index-1]
		
	#Solution 4 - Predict Rival, lose
	solutions[4]='';
	len=8
	index=-1
	while(index==-1 and len>0):
		index=rivalHistory.find(rivalHistory[0:len-1],1);
		len-=1;
	if(len!=0):
		expetctedR=rivalHistory[index-1]
		if expetctedR=='R':
			solutions[4]= "S" 
		elif expetctedR=='P':
			solutions[4] = "R" 
		else:
			solutions[4] = "P"
			
	#Solution 5 - Predict self, repeat
	solutions[5]='';
	len=8
	index=-1
	while(index==-1 and len>0):
		index=selfHistory.find(selfHistory[0:len-1],1);
		len-=1;
	if(len!=0):
		solutions[5]=selfHistory[index-1]
		
	#Solution 6 - Predict self, tie
	solutions[6]='';
	len=8
	index=-1
	while(index==-1 and len>0):
		index=selfHistory.find(selfHistory[0:len-1],1);
		len-=1;
	if(len!=0):
		expetctedS=selfHistory[index-1]
		if expetctedS=='R':
			solutions[6] = "P"
		elif expetctedS=='P':
			solutions[6] = "S"
		else:
			solutions[6] = "R"
			
	#Solution 7 - Repeat Self
	solutions[7]=output;
	
	#Solution 8 - Repeat Rival
	solutions[8]=input;
	
	#Solution 9 - Rival assumes repeating
	expetctedS=output
	if expetctedS=='R':
		solutions[9] = "S"
	elif expetctedS=='P':
		solutions[9] = "R"
	else:
		solutions[9] = "P"
			
	best=0
	besti=-1;
	for i in range(0,9):
		if(scores[i]>best and solutions[i]!=''):
			best=scores[i]
			besti=i
			output=solutions[i];
	scores[besti]-=1;
	selfHistory=output+selfHistory;