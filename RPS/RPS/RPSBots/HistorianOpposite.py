# remembers moves and beats the least frequent
# -vladh
import random;

def beat(move):
	if move=="R": return "P";
	if move=="P": return "S";
	if move=="S": return "R";
	return None;
def numToMove(num):
	if num==0: return "R";
	if num==1: return "P";
	if num==2: return "S";
	return None;

if input=="":
	history="";
else:
	history+=input;

f=[0,0,0];
for i in history:
	if i=="R": f[0]+=1;
	if i=="P": f[1]+=1;
	if i=="S": f[2]+=1;
	
output=beat(numToMove(f.index(min(f))));