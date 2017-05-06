from random import choice
from zlib import compress

if input == "":
	anteriores = ""
	output = choice(["R", "P", "S"])
else:
	anteriores += input
	r = len(compress(anteriores + "R"))
	p = len(compress(anteriores + "P"))
	s = len(compress(anteriores + "S"))
	if r < p and r < s:	# Shorter length means higher probability
		output = "P"	# Paper beats Rock
	elif p < s:
		output = "S"	# Scissors beats Paper
	else:
		output = "R"	# Rock beats Scissors