#why ? 
import random
if input == "":
	output = random.choice(["R", "P", "S"])
	beat = {'P': 'S', 'S': 'R', 'R': 'P'}
  	beat2 = {'PP': 'S', 'SS': 'R', 'RR':'P', 'PS': 'S', 'PR': 'P', 'RS': 'R', 'RP': 'P', 'SP': 'S', 'SR': 'R'}
	oppH = myH =[]
else:	
	oppH.append(input)
	myH.append(output)
	output = beat2[random.choice(oppH) + beat2[random.choice(myH)+random.choice(["R", "P", "S"])]]