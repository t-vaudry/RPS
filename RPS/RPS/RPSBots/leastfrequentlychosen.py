import random
rockCount = paperCount = scissorCount = 0

# gets a random choice
def randomChoice():
	choice=random.randint(1,3)
	# print choice
	if choice == 1:
		return "R"
	elif choice == 2: 
		return "P"
	elif choice==3:
		return "S"

# determines if there is a unique least choice
def leastUsed():
	if history[0] < history[1] and history[0] < history[2]:
		return "P" #rock is min, paper beats rock
	elif history[1] < history[0] and history[1] < history[2]:
		return "S" #paper is min, scissor beats rock
	elif history[2] < history[0] and history[2] < history[1]:
		return "R" #scissor is min, rock beats rock
	else:
		return randomChoice()

# keep track of choices
if input=="":
	output = randomChoice()
elif input=="R":
	rockCount = rockCount +1
elif input == "P":
	paperCount = paperCount +1
elif input == "S":
	scissorCount = scissorCount +1

history = [rockCount, paperCount, scissorCount]

# output will beat the least used choice or
# will be random if no least choice
output = leastUsed()