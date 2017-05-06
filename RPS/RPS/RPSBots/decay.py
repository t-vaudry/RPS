from random import random
from math import exp
if input == "": # initialize variables for the first round
	r = p = s = 0
elif input == "R":
	p += .1
	s -= .1
elif input == "P":
	s += .1
	r -= .1
elif input == "S":
	r += .1
	p -= .1
r=.95*r
p=.95*p
s=.95*s

rand = random() * (exp(r)+exp(p)+exp(s))
if rand < exp(r):
	output = "R"
elif rand < exp(r) + exp(p):
	output = "P"
else:
	output = "S"