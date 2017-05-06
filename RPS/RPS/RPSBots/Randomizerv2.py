import random
random.seed(random.choice([1,54,5,4,89,54,7,9,54,7,4]))
if input == "":
	RC = PC = SC = 0
	RC += random.choice([1,2,3])
	PC += random.choice([1,2,3])
	SC += random.choice([1,2,3])
elif input == "R":
	RC += 1
elif input == "P":
	PC += 1
elif input == "S":
	SC += 1
if RC > PC and RC > SC:
	output = "P"
elif PC > SC:
	output = "S"
else:
	output = "R"