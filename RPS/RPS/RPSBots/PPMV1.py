import random

# initialization
if input=="":
	maxHistoryLength = 200
	history = ""
	dictionary = {}

# update history
history += input
if len(history) > maxHistoryLength:
	history = history[1:maxHistoryLength+1]

# update dictionary
index = 0
while index < len(history):
	key = history[index:len(history)]
	if dictionary.has_key(key):
		dictionary[key] = dictionary[key] + 1
	else:
		dictionary[key] = 1
	index+=1

# make prediction
order = len(history)-1
output = ""
while order >= 0:
	context = history[len(history)-order:len(history)]
	if dictionary.has_key(context+"R"):
		rockCount = dictionary[context+"R"]
	else:
		rockCount = 0
	if dictionary.has_key(context+"P"):
		paperCount = dictionary[context+"P"]
	else:
		paperCount = 0
	if dictionary.has_key(context+"S"):
		scissorsCount = dictionary[context+"S"]
	else:
		scissorsCount = 0
	if rockCount > paperCount and rockCount > scissorsCount:
		output = "P"
	elif paperCount > scissorsCount:
		output = "S"
	else:
		output = "R"
	order -= 1
	if output != "":
		break
if output == "":
	output=random.choice(["R","P","S"])