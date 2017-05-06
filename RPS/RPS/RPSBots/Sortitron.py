import random

# choose rps strategy

if input == "": 
	# initialize variables for the first round
	rockCount = paperCount = scissorsCount = 0

elif input == "R":
	rockCount += 1
elif input == "P":
	paperCount += 1
elif input == "S":
	scissorsCount += 1
Count = rockCount = paperCount = scissorsCount


if rockCount == paperCount == scissorsCount:
    output = random.choice(["R","P","S"])
elif Count > 0:

	# record past choices
	# store value in an array

	for i in range(int(Count)):
		array = []
		if input == "R":
			array[i] = "R"
		elif input == "P":
			array[i] = "P"
		elif input == "S":
			array[i] = "S"
		
	# sort list of past

	array.sort();

	# frequency analysis

	spectrum = random.randint(0,1000)

	# modify strategy

	if spectrum in range(0,10):
		output = "R"
	elif spectrum in range(10, 20):
		output = "P"
	elif spectrum in range(20,30):
		output = "S"