import random

if input == "":
	r = 1
        p = 0
        s = 0
        output = "R"
elif r <=p and r <=s:
	r += 1
        output = "R"
elif p <=r and p <=s:
	p += 1
        output = "P"
elif s <=r and s <=p:
	s += 1
        output = "S"