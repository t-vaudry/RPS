import random
#Using an infographic about the psychology of RPS
#from the world RPS secioty, I made this reflect that.
output = ""
while True:
	if input == "":
		history = []
		history.append(input)
		output = "S"
		break
	elif len(history)== 1:
		history.append(input)
		output = "S"
		break
	else:
		prev = history.pop()
		prev2 = history.pop()
		history.append(prev2)
		history.append(prev)
		history.append(input)
		#People rarely if ever like to repeat three times
		#If duplicates, return one of the two counter moves.
		if prev == prev2:
			choice = random.choice([True, False])
			if prev == "R":
				if choice == True:
					output = "P"
					break
				else:
					output = "S"
					break
			elif prev == "P":
				if choice == True:
					output = "R"
					break
				else:
					output = "S"
					break
			else:
				
				if choice == True:
					output = "R"
					break
				else:
					output = "P"
					break
		#People who throw paper will likely expect you to throw rock next
		#Counter that with scissors.
		elif prev == "R":
			output = "S"
			break
		#Paper is only statistically thrown 29.6% of the time
		#If nothing else catches it, go for the least thrown
		else:
			output = "P"
			break