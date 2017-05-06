if input == "": # initialize variables for the first round
	r = p = s = 0
elif input == "R":
	r += 1
elif input == "P":
	p += 1
elif input == "S":
	s += 1
if r > p and r > s:
	output = "R" # paper beats rock
elif p > s:
	output = "P" # scissors beats paper
else:
	output = "S" # rock beats scissors