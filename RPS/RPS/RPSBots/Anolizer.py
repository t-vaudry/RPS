if input == "":
	rock = paper = scissor = myp = myr = mys = beat = 0
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

if play >= 100:
	if beat > play/2 + 20:
		{'R': 'S', 'P': 'R', 'S': 'P'}[input]
elif rock > mys and paper > myr and scissor > myp:
	if rock < paper and rock < scissor:
		output = 'R'
	elif paper < scissor:
		output = 'P'
	else:
		output = 'S'

if output == 'R':
	myr += 1
elif output == 'P':
	myp += 1
else:
	mys += 1

last_output = output