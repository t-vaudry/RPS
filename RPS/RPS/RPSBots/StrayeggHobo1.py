# Strayegg Hobo
# Simon Hooker / Aeiedil (simon@strayegg.com)
# The hobo is a simple beast that just takes a guess based on no good logic at alll, hooray

# config if match start
import random

if not input:
	# new batch
	ursum = 0
	validoptions = ["S","P","R"]
	# choose a random
	output=random.choice(validoptions)
else:
	# input will be R P or S
	# add to sums and mod
	for index,item in enumerate(validoptions):
		if item==input:
			ursum = (ursum+index+1)%3
	output = validoptions[(ursum+1)%3]