# Necklacebot
#
# I chose this name because...
#
# It tries to tie.
# Geddit? :D
#
# By cjfaure.

import random

if input: # not the first round
	history[1] += input
	sf = sorted("RPS", key=lambda x: (history[1][::-1]+"PSR").index(x))
	history[0] += random.choice(sf[0]+sf[2])
else: # initialize ALL da variables!
	history = [random.choice("RPS"), ""]

output = history[0][-1]