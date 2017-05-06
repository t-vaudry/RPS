import random
if input == '':
	output = random.choice(["R","P","S"])
elif input == "R": 
	output = "P" 
elif input == "P": 
	output = "S"
elif input == "S": 
	output = "R"