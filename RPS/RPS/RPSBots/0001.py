import random
if input == '':
	output = random.choice(["R","P","S"])
elif input == "R": 
	output = "S" 
elif input == "P": 
	output = "R"
elif input == "S": 
	output = "P"