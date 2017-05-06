import random
s = 5
if input == "":
	output = random.choice(["R", "P", "S"])
	rps_next = {'P': 'S', 'S': 'R', 'R': 'P'}
	h = ""
else:
	h += input + output
	output = rps_next[random.choice(h+h[-s:]+h[-2*s:]+h[-3*s:])]