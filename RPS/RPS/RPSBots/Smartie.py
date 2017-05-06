import random

if input == "":
	plays = {"R": [],
			 "P": [],
			 "S": []}
	beats = {"R": "S","P": "R","S": "P"}
	output = random.choice(["R","P","S"])
else:
	plays[mylast].append(input)
	try:
		output = random.choice(plays[mylast])
	except IndexError:
		output = random.choice(["R","P","S"])

mylast = output