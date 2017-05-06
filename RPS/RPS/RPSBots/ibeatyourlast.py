import random

# testing
# input = ""
# input = "R"
# input = "P"
# input = "S"

def randomChoice():
	choice=random.randint(1,3)
	# print choice
	if choice == 1:
		return "R"
	elif choice == 2: 
		return "P"
	elif choice==3:
		return "S"

if input=="":
	output = randomChoice()
elif input=="R":
	output = "P"
elif input == "P":
	output="S"
elif input == "S":
	output="R"		

#print output