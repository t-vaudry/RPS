#Switchy is broken!

def shiftUp(x):
	if x == "R":
		return "P"
	if x == "P":
		return "S"
	return "R"
def shiftDown(x):
	if x == "R":
		return "S"
	if x == "P":
		return "R"
	return "P"
def c(x,y):
	if x == y:
		return "tie"
	if shiftUp(y) == x:
		return "win"
	return "lose"

if input == "":
	output = "R"
	last = "R"
else:
	if input == last:
		output = shiftUp(input)
	elif input == shiftUp(last):
		output = input
	else:
		output = shiftDown(input)
last = output