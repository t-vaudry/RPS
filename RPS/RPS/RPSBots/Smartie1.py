import random

if input == "":
	plays = {"R": [],
			 "P": [],
			 "S": []}
	beats = {"R": "P","P": "S","S": "R"}
	shifted = beats
	output = random.choice(["R","P","S"])
else:
	plays[mylast].append(input)
	try:
		output = shifted[random.choice(plays[input])]
	except IndexError:
		output = random.choice(["R","P","S"])

	if beats[mylast] == input:
		shifted = {"R": shifted["P"], "P": shifted["S"], "S": shifted["R"]}

mylast = output