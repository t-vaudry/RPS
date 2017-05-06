# Last try for me tonight
import random
if input == "":
	rock = paper = scissor = beat = 0
	play = 0
	last_output = 'R'

result = {'R':'P', 'P':'S', 'S':'R'}[last_output]
if result == input:
	beat += 1

if input == "R":
	rock += 1
	output = "P"
elif input == "P":
	paper += 1
	output = "S"
elif input == "S":
	scissor += 1
	output = "R"
else:
	output = 'P'

play += 1

if play >= 40:
	if beat > play/2:
		{'R':'P', 'P':'S', 'S':'R'}[output]
else:
	output = random.choice(["R", "P", "S"])

last_output = output