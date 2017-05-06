R=1;
P=2;
S=3;

if input == "": # initialize variables for the first round
	ins = [] 
elif input == "R":
	ins.append(R)
elif input == "P":
	ins.append(P)
elif input == "S":
	ins.append(S)

tot=sum(ins) -3*((sum(ins)+2)/3) + 1

if tot == 1:
	output="R"
elif tot == 2:
	output="R"
elif tot == 3:
	output="R"