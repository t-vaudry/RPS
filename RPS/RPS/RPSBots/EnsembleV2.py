# initialization
if input=="":
	maxHistoryLength = 5
	numPredictors = (maxHistoryLength+2)*3
	scores = []
	index = 0
	while index < numPredictors:
		scores.append(1.0)
		index+=1
	totalScore = 1.0*numPredictors
	history = ""
	dictionary = {}
	predictions = ["R", "P", "S"]
	index = 3
	while index < numPredictors:
		predictions.append("")
		index+=1

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

# update scores
index = 0
while index < numPredictors:
	if predictions[index] == input:
		scores[index] += 1.0
		totalScore += 1.0
	index+=1

# make predictions
order = 0
index = 3
while order <= maxHistoryLength:
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
		predictions[index] = "R"
		predictions[index+1] = "P"
		predictions[index+2] = "S"
	elif paperCount > scissorsCount:
		predictions[index] = "P"
		predictions[index+1] = "S"
		predictions[index+2] = "R"
	else:
		predictions[index] = "S"
		predictions[index+1] = "R"
		predictions[index+2] = "P"
	index += 3
	order += 1

# choose move
rock = 0
paper = 0
scissors = 0
index = 0
while index < numPredictors:
	if predictions[index] == "R":
		rock += scores[index]/totalScore
	elif predictions[index] == "P":
		paper += scores[index]/totalScore
	else:
		scissors += scores[index]/totalScore
	index += 1
if rock > paper and rock > scissors:
	output = "P"
elif paper > scissors:
	output = "S"
else:
	output = "R"