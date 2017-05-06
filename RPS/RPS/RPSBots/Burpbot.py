# burpbot
# by cjfaure

# let's see how it does :)

# calibrated against the leaderboard.

from random import choice
from random import random

if input:
	h[1].append(input)
	l = sorted([[h[1].count(i)/len(h[1]), i] for i in "RPS"], key=lambda c:c[0]+random()/2)[0][1]
	# l is the move that the opponent's played least.
	# let's choose another.
	pm = ["R", "P", "S", beats[l]]
	for i in [l, h[0][-3%len(h[0])]]:
		if i in pm:
			del pm[pm.index(i)]
	h[0].append(choice(pm))
	# ...unless we want to be unpredictable.
	if random() < 0.7: h[0][-1] = l
else:
	h = [[choice(["R", "P", "S"])], []]
	beats = {"R": "S", "P": "R", "S": "P"}
output = h[0][-1]