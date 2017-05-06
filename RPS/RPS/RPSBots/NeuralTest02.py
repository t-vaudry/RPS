import random

#Attempt to predict the responses by using a single layer neural network with a "State" feedback 
#Modified the back propagation a tad


if (input == ""):

        Synapses = {};
        In_Nodes = {};
	Out_Nodes = {};
	Error_Nodes = {};
	i = 0;
	j = 0;
	Alpha = 0.01;

	for i in range(0,7):
		for j in range(0,4):
			Synapses[(i,j)] = random.random() - 0.5;
			
	for i in range(0,7):
		In_Nodes[i] = 0;
	
	for i in range(0,4):
		Out_Nodes[i] = 0;
		Error_Nodes[i] = 0;
		
        output = "R";

else:

	#Given the previous history and state, what should the output have been to win
	
	if (input == "R"):
		In_Nodes[0] = 1;
		In_Nodes[1] = 0;
		In_Nodes[2] = 0;
	elif (input == "P"):
		In_Nodes[0] = 0;
		In_Nodes[1] = 1;
		In_Nodes[2] = 0;
	elif (input == "S"):
		In_Nodes[0] = 0;
		In_Nodes[1] = 0;
		In_Nodes[2] = 1;
		
	if (output == "R"):
		In_Nodes[3] = 1;
		In_Nodes[4] = 0;
		In_Nodes[5] = 0;
	elif (output == "P"):
		In_Nodes[3] = 0;
		In_Nodes[4] = 1;
		In_Nodes[5] = 0;
	elif (output == "S"):
		In_Nodes[3] = 0;
		In_Nodes[4] = 0;
		In_Nodes[5] = 1;
		
	In_Nodes[6] = Out_Nodes[3];
	
	for i in range(0,4):
		Out_Nodes[i] = 0;
		for j in range(0,7):
			Out_Nodes[i] += (Synapses[(j,i)] * In_Nodes[j]);
	
	#What should the network output have been
	
	if (input == "R"):
		#Output should have been "P"
		Error_Nodes[0] = 0 - Out_Nodes[0];
		Error_Nodes[1] = 1 - Out_Nodes[1];
		Error_Nodes[2] = 0 - Out_Nodes[2];
	elif (input == "P"):
		#Output should have been "S"
		Error_Nodes[0] = 0 - Out_Nodes[0];
		Error_Nodes[1] = 0 - Out_Nodes[1];
		Error_Nodes[2] = 1 - Out_Nodes[2];
	elif (input == "S"):
		#Output should have been "R"
		Error_Nodes[0] = 1 - Out_Nodes[0];
		Error_Nodes[1] = 0 - Out_Nodes[1];
		Error_Nodes[2] = 0 - Out_Nodes[2];
		
	#Backpropogate
	
	for i in range(0,4):
		for j in range(0,7):
			Synapses[(j,i)] = Synapses[(j,i)] + Alpha*Error_Nodes[i];
			
	#Try and select next output
	
	if (input == "R"):
		In_Nodes[0] = 1;
		In_Nodes[1] = 0;
		In_Nodes[2] = 0;
	elif (input == "P"):
		In_Nodes[0] = 0;
		In_Nodes[1] = 1;
		In_Nodes[2] = 0;
	elif (input == "S"):
		In_Nodes[0] = 0;
		In_Nodes[1] = 0;
		In_Nodes[2] = 1;
		
	if (output == "R"):
		In_Nodes[3] = 1;
		In_Nodes[4] = 0;
		In_Nodes[5] = 0;
	elif (output == "P"):
		In_Nodes[3] = 0;
		In_Nodes[4] = 1;
		In_Nodes[5] = 0;
	elif (output == "S"):
		In_Nodes[3] = 0;
		In_Nodes[4] = 0;
		In_Nodes[5] = 1;
		
	In_Nodes[6] = Out_Nodes[3];
	
	for i in range(0,4):
		Out_Nodes[i] = 0;
		for j in range(0,7):
			Out_Nodes[i] += (Synapses[(j,i)] * In_Nodes[j]);
			
	if (Out_Nodes[0] > Out_Nodes[1]) and (Out_Nodes[0] > Out_Nodes[2]):
		output = "R";
	elif (Out_Nodes[1] > Out_Nodes[0]) and (Out_Nodes[1] > Out_Nodes[2]):
		output = "P";
	elif (Out_Nodes[2] > Out_Nodes[0]) and (Out_Nodes[2] > Out_Nodes[1]):
		output = "S";
	else:
		output = random.choice(["R","P","S"]);