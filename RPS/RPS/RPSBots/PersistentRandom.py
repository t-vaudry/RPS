# picks a move and plays it multiple times
import random;

def numToMove(num):
	if num==0: return "R";
	if num==1: return "P";
	if num==2: return "S";
	return None;
if input=="":
	do=["R",0];

if do[1]==0:
	print "bla";
	do[0]=numToMove(random.randrange(0,2));
	do[1]=random.randrange(3,8);

do[1]-=1;
output=do[0];