if input == "":
	r = p = s = 0

elif input == "R":
	r += 1
elif input == "P":
	p += 1
elif input == "S":
	s += 1

if r > p and r > s:
	output = "P"
elif p > s:
	output = "S"
else:
	output = "R"