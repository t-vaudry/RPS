# Bobby 1
# I'm new to this kind of thing...

import random

# Store the values of this input and the input before it.
if input == "":
	a = ""
	b = ""
else:
	a = b
	b = input

if a == b: # If the inputs are equal, assume the human will change.
	if b == "R": # Human will change to either scissors or paper.
		output = "S"
	elif b == "S": # Human will change to either rock or paper.
		output = "P"
	elif b == "P": # Human will change to either rock or scissors.
		output = "R"
	elif b == "": # This is the first turn, make a random choice.
		output = random.choice(["R", "S", "P"])
else: # If the inputs are not equal,
	if a == "R":
		if b == "S": # Predict P.
			output = "S"
		elif b == "P": # Predict S.
			output = "R"
	elif a == "S":
		if b == "R": # Predict P.
			output = "S"
		elif b == "P": #Predict R.
			output = "P"
	elif a == "P":
		if b == "S": # Predict R.
			output = "P"
		elif b == "R": # Predict S.
			output = "R"
output = random.choice(["R", "S", "P"]) # If it somehow ends up here...